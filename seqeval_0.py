
real_label = ['B', 'O', 'O', 'B', 'I', 'I', 'S', 'B', 'I', 'I', 'E']
pred_label = ['B', 'O', 'O', 'B', 'I', 'I', 'I', 'I', 'I', 'I', 'I']


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
    num_pred_correct = 0
    b1 = b2 = 0

    for i in range(len(l1)):
        if l2[i] == 'B':
            b2 += 1

        if l1[i] == 'B':
            b1 += 1
            if l2[i] == 'B':
                num_pred_correct += 1
            else:
                continue
        else:
            continue

    precision = num_pred_correct / b2
    recall = num_pred_correct / b1
    f1_score = 2 * precision * recall / (precision + recall)

    return precision, recall, f1_score


# Jaccard Similarity
def jaccard_sim(l1, l2):
    l1 = set(l1)
    # print(len(l1))
    l2 = set(l2)
    # print(len(l2))
    a = l1.intersection(l2)
    # print(len(a))
    return float(len(a) / (len(l1) + len(l2) - len(a)))


print('Strict完全匹配：\nPrecision = {:.2f}\nRecall = {:.2f}\nF1_score = {:.2f}\n'.format(strict_mat(real_label, pred_label)[0], strict_mat(real_label, pred_label)[1], strict_mat(real_label, pred_label)[2]))
print('只匹配Begin：\nPrecision = {:.2f}\nRecall = {:.2f}\nF1_score = {:.2f}\n'.format(beginOnly(real_label, pred_label)[0], beginOnly(real_label, pred_label)[1], beginOnly(real_label, pred_label)[2]))
print('Jaccard部分匹配：\nJaccard Similarity = {:.2f}\n'.format(jaccard_sim(real_label, pred_label)))

