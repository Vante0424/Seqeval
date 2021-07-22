
def getLabels(filename):
    with open(filename, 'r', encoding='utf-8') as f:
        values = f.readlines()
        values = [item for item in values]
        training_data = []

        for i in range(len(values)):
            values_i = eval(values[i])
            training_data.append(values_i['labels'])
    # print(training_data)

    return training_data


list1 = getLabels('train--.txt')
list2 = getLabels('pred--.txt')
# print(list1)
# print(list2)


# Strict Matching
def strict_mat(l1, l2):
    num_all = 0
    num_pred_correct = 0

    for i in range(len(l1)):
        for j in range(len(l2[i])):
            if l1[i][j] == l2[i][j]:
                num_pred_correct += 1
        num_all += j + 1

    # print(num_all)

    precision = num_pred_correct / num_all
    recall = num_pred_correct / num_all
    f1_score = 2 * precision * recall / (precision + recall)

    return precision, recall, f1_score

# print(strict_mat(list1, list2))


# Only Begin
def beginOnly(l1, l2):
    num_pred_correct_src = 0
    num_pred_correct_cue = 0
    num_pred_correct_con = 0
    b1_src = b1_cue = b1_con = b2_src = b2_cue = b2_con = 0

    for i in range(len(l1)):
        for j in range(len(l2[i])):
            if l1[i][j].startswith('B'):
                if 'source' in l1[i][j]:
                    b1_src += 1
                elif 'cue' in l1[i][j]:
                    b1_cue += 1
                elif 'content' in l1[i][j]:
                    b1_con += 1

            if l2[i][j] == 'B-source':
                b2_src += 1
                if l1[i][j] == l2[i][j]:
                    num_pred_correct_src += 1
            elif l2[i][j] == 'B-cue':
                b2_cue += 1
                if l1[i][j] == l2[i][j]:
                    num_pred_correct_cue += 1
            elif l2[i][j] == 'B-content':
                b2_con += 1
                if l1[i][j] == l2[i][j]:
                    num_pred_correct_con += 1

    # print(b1_src, b2_src)
    # print(b1_cue, b2_cue)
    # print(b1_con, b2_con)
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

# beginOnly(list1, list2)


# Jaccard Similarity
def jaccard_sim(l1, l2):
    ls1 = ls2 = []
    for i in range(len(l1)):
        for j in range(len(l1[i])):
            ls1.append(l1[i][j])
            ls2.append(l2[i][j])

    l1 = set(ls1)
    # print(len(l1))
    l2 = set(ls2)
    # print(len(l2))
    a = l1.intersection(l2)
    # print(len(a))
    return float(len(a) / (len(l1) + len(l2) - len(a)))

# jaccard_sim(list1, list2)

print('Strict完全匹配：\nPrecision = {:.2f}\nRecall = {:.2f}\nF1_score = {:.2f}\n'.format(strict_mat(list1, list2)[0], strict_mat(list1, list2)[1], strict_mat(list1, list2)[2]))
print('只匹配Begin：\n'
      'source:\nPrecision = {:.2f}\nRecall = {:.2f}\nF1_score = {:.2f}\n'
      'cue:\nPrecision = {:.2f}\nRecall = {:.2f}\nF1_score = {:.2f}\n'
      'content:\nPrecision = {:.2f}\nRecall = {:.2f}\nF1_score = {:.2f}\n'.format(beginOnly(list1, list2)[0][0], beginOnly(list1, list2)[0][1], beginOnly(list1, list2)[0][2],
                                                                                  beginOnly(list1, list2)[1][0], beginOnly(list1, list2)[1][1], beginOnly(list1, list2)[1][2],
                                                                                  beginOnly(list1, list2)[2][0], beginOnly(list1, list2)[2][1], beginOnly(list1, list2)[2][2]))
print('Jaccard部分匹配：\nJaccard Similarity = {:.2f}\n'.format(jaccard_sim(list1, list2)))

