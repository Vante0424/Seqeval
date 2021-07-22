
real_label = ['B', 'O', 'O', 'B', 'I', 'I', 'S', 'B', 'I', 'I', 'E']
pred_label = ['B', 'O', 'O', 'B', 'I', 'I', 'I', 'I', 'I', 'I', 'I']

real_data = [{"en": "O"}, {"en": "B-source"}, {"en": "I-source"}, {"en": "B-cue"},
             {"en": "I-cue"}, {"en": "B-content"}, {"en": "I-content"}]
pred_data = [{"en": "B-source"}, {"en": "B-source"}, {"en": "I-source"}, {"en": "B-cue"},
             {"en": "I-cue"}, {"en": "B-content"}, {"en": "O"}]

real_values = [item[key] for item in real_data for key in item]
print(real_values)
# for item in data:
#    for key in item:
#       print(item[key])
pred_values = [item[key] for item in pred_data for key in item]
print(pred_values)

# if 'source' in pred_values[0]:
#     print(1)


# Strict Matching
def strict_mat(l1, l2):
    num_label = len(l1)
    num_pred = len(l2)
    num_pred_correct = 0

    for i in range(num_label):
        if l1[i] == l2[i]:
            num_pred_correct += 1

    # print(num_label)
    # print(num_pred)
    # print(num_pred_correct)

    precision = num_pred_correct / num_pred
    recall = num_pred_correct / num_label
    f1_score = 2 * precision * recall / (precision + recall)

    return precision, recall, f1_score


# Only Begin
def beginOnly(l1, l2):
    num_pred_correct_src = 0
    num_pred_correct_cue = 0
    num_pred_correct_con = 0
    b1_src = b1_cue = b1_con = b2_src = b2_cue = b2_con = 0

    for i in range(len(l1)):
        if l1[i].startswith('B'):
            if 'source' in l1[i]:
                b1_src += 1
            elif 'cue' in l1[i]:
                b1_cue += 1
            elif 'content' in l1[i]:
                b1_con += 1

        if l2[i].startswith('B'):
            if 'source' in l2[i]:
                b2_src += 1
                if 'source' in l2[i]:
                    num_pred_correct_src += 1
            elif 'cue' in l2[i]:
                b2_cue += 1
                if 'cue' in l2[i]:
                    num_pred_correct_cue += 1
            elif 'content' in l2[i]:
                b2_con += 1
                if 'content' in l2[i]:
                    num_pred_correct_con += 1

            # if l1[i].startswith('B'):
            #     if 'source' in l1[i] and 'source' in l2[i]:
            #         num_pred_correct_src += 1
            #     elif 'cue' in l1[i] and 'cue' in l2[i]:
            #         num_pred_correct_cue += 1
            #     elif 'content' in l1[i] and 'content' in l2[i]:
            #         num_pred_correct_con += 1
            # else:
            #     continue

    # print(b1, b2)
    # print(num_pred_correct_src, num_pred_correct_cue, num_pred_correct_con)

    precision_src = num_pred_correct_src / b2_src
    recall_src = num_pred_correct_src / b1_src
    f1_score_src = 2 * precision_src * recall_src / (precision_src + recall_src)

    precision_cue = num_pred_correct_cue / b2_cue
    recall_cue = num_pred_correct_cue / b1_cue
    f1_score_cue = 2 * precision_cue * recall_cue / (precision_cue + recall_cue)

    precision_con = num_pred_correct_con / b2_con
    recall_con = num_pred_correct_con / b1_con
    f1_score_con = 2 * precision_con * recall_con / (precision_con + recall_con)

    return (precision_src, recall_src, f1_score_src), (precision_cue, recall_cue, f1_score_cue), (precision_con, recall_con, f1_score_con)


# Jaccard Similarity
def jaccard_sim(l1, l2):
    l1 = set(l1)
    # print(len(l1))
    l2 = set(l2)
    # print(len(l2))
    a = l1.intersection(l2)
    # print(len(a))
    return float(len(a) / (len(l1) + len(l2) - len(a)))


print('Strict完全匹配：\nPrecision = {:.2f}\nRecall = {:.2f}\nF1_score = {:.2f}\n'.format(strict_mat(real_values, pred_values)[0], strict_mat(real_values, pred_values)[1], strict_mat(real_values, pred_values)[2]))
print('只匹配Begin：\n'
      'source:\nPrecision = {:.2f}\nRecall = {:.2f}\nF1_score = {:.2f}\n'
      'cue:\nPrecision = {:.2f}\nRecall = {:.2f}\nF1_score = {:.2f}\n'
      'content:\nPrecision = {:.2f}\nRecall = {:.2f}\nF1_score = {:.2f}\n'.format(beginOnly(real_values, pred_values)[0][0], beginOnly(real_values, pred_values)[0][1], beginOnly(real_values, pred_values)[0][2],
                                                                                  beginOnly(real_values, pred_values)[1][0], beginOnly(real_values, pred_values)[1][1], beginOnly(real_values, pred_values)[1][2],
                                                                                  beginOnly(real_values, pred_values)[2][0], beginOnly(real_values, pred_values)[2][1], beginOnly(real_values, pred_values)[2][2]))
print('Jaccard部分匹配：\nJaccard Similarity = {:.2f}\n'.format(jaccard_sim(real_values, pred_values)))

