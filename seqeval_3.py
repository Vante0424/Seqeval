from sklearn.metrics import accuracy_score, precision_score, recall_score, f1_score


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


list1 = getLabels('train.txt')
list2 = getLabels('pred.txt')
print(list1)
print(list2)

# list1 = [['B-source', 'I-source', 'I-source', 'B-cue', 'I-cue', 'I-cue'], ['B-source', 'I-source', 'I-source', 'B-content', 'I-content', 'I-content', 'O']]
# source[0, 3)[0, 3)cue[3, 6)content[0, 3)
# list2 = [['B-source', 'I-source', 'I-content', 'I-cue', 'B-cue', 'I-cue'], ['B-source', 'I-source', 'I-source', 'B-content', 'I-content', 'I-content', 'O']]
# source[0, 2)[0, 3)cue[4, 6)content[0, 3)


def strict_matching(l1, l2):
    true_src = []
    pred_src = []
    true_cue = []
    pred_cue = []
    true_con = []
    pred_con = []

    # source
    for i in range(len(l1)):
        # 正
        flag_src = False
        for j in range(len(l1[i])):
            if l1[i][j] == 'B-source':
                startidx1_src = j
                # print(startidx1_src)
                for k in range(j+1, len(l1[i])-1):
                    # print(l1[i][k])
                    if l1[i][k] != 'I-source' or k == len(l1[i])-1:
                        # print(k)
                        endidx1_src = k
                        break
                true_src.append(1)
            # print(startidx1, endidx1)

            if l2[i][j] == 'B-source':
                startidx2_src = j
                for k in range(j+1, len(l2[i])-1):
                    if l2[i][k] != 'I-source' or k == len(l1[i])-1:
                        endidx2_src = k
                        break
                if startidx1_src == startidx2_src and endidx1_src == endidx2_src:
                    pred_src.append(1)
                    flag_src = True  # 设置标志位，如果完全匹配则不用逆向
                else:
                    pred_src.append(0)
                    flag_src = False
            # print(startidx2, endidx2)

        # 逆
        if not flag_src:
            for j in range(len(l2[i])):
                if l2[i][j] == 'B-source':
                    startidx2_src = j
                    for k in range(j + 1, len(l2[i]) - 1):
                        # print(l2[i][k])
                        if l2[i][k] != 'I-source' or k == len(l1[i])-1:
                            # print(k)
                            endidx2_src = k
                            break
                    pred_src.append(1)
                # print(startidx2, endidx2)

                if l1[i][j] == 'B-source':
                    startidx1_src = j
                    for k in range(j + 1, len(l1[i]) - 1):
                        if l1[i][k] != 'I-source' or k == len(l1[i])-1:
                            endidx1_src = k
                            break
                    if startidx1_src == startidx2_src and endidx1_src == endidx2_src:
                        true_src.append(1)
                    else:
                        true_src.append(0)
                # print(startidx1, endidx1)
    # print(true_src)
    # print(pred_src)

    # cue
    for i in range(len(l1)):
        # 正
        flag_cue = False
        for j in range(len(l1[i])):
            if l1[i][j] == 'B-cue':
                startidx1_cue = j
                for k in range(j + 1, len(l1[i]) - 1):
                    # print(l1[i][k])
                    if l1[i][k] != 'I-cue' or k == len(l1[i])-1:
                        # print(k)
                        endidx1_cue = k
                        break
                true_cue.append(1)
            # print(startidx1, endidx1)

            if l2[i][j] == 'B-cue':
                startidx2_cue = j
                for k in range(j + 1, len(l2[i]) - 1):
                    if l2[i][k] != 'I-cue' or k == len(l1[i])-1:
                        endidx2_cue = k
                        break
                if startidx1_cue == startidx2_cue and endidx1_cue == endidx2_cue:
                    pred_cue.append(1)
                    flag_cue = True  # 设置标志位，如果完全匹配则不用逆向
                else:
                    pred_cue.append(0)
                    flag_cue = False
            # print(startidx2, endidx2)

        # 逆
        if not flag_cue:
            for j in range(len(l2[i])):
                if l2[i][j] == 'B-cue':
                    startidx2_cue = j
                    for k in range(j + 1, len(l2[i]) - 1):
                        # print(l2[i][k])
                        if l2[i][k] != 'I-cue' or k == len(l1[i])-1:
                            # print(k)
                            endidx2_cue = k
                            break
                    pred_cue.append(1)
                # print(startidx2, endidx2)

                if l1[i][j] == 'B-cue':
                    startidx1_cue = j
                    for k in range(j + 1, len(l1[i]) - 1):
                        if l1[i][k] != 'I-cue' or k == len(l1[i])-1:
                            endidx1_cue = k
                            break
                    if startidx1_cue == startidx2_cue and endidx1_cue == endidx2_cue:
                        true_cue.append(1)
                    else:
                        true_cue.append(0)
                # print(startidx1, endidx1)
    # print(true_cue)
    # print(pred_cue)

    # content
    for i in range(len(l1)):
        # 正
        flag_con = False
        for j in range(len(l1[i])):
            if l1[i][j] == 'B-content':
                startidx1_con = j
                for k in range(j + 1, len(l1[i]) - 1):
                    # print(l1[i][k])
                    if l1[i][k] != 'I-content' or k == len(l1[i])-1:
                        # print(k)
                        endidx1_con = k
                        break
                true_con.append(1)
            # print(startidx1, endidx1)

            if l2[i][j] == 'B-content':
                startidx2_con = j
                for k in range(j + 1, len(l2[i]) - 1):
                    if l2[i][k] != 'I-content' or k == len(l1[i])-1:
                        endidx2_con = k
                        break
                if startidx1_con == startidx2_con and endidx1_con == endidx2_con:
                    pred_con.append(1)
                    flag_con = True  # 设置标志位，如果完全匹配则不用逆向
                else:
                    pred_con.append(0)
                    flag_con = False
            # print(startidx2, endidx2)

        # 逆
        if not flag_con:
            for j in range(len(l2[i])):
                if l2[i][j] == 'B-content':
                    startidx2_con = j
                    for k in range(j + 1, len(l2[i]) - 1):
                        # print(l2[i][k])
                        if l2[i][k] != 'I-content' or k == len(l1[i])-1:
                            # print(k)
                            endidx2_con = k
                            break
                    pred_con.append(1)
                # print(startidx2, endidx2)

                if l1[i][j] == 'B-content':
                    startidx1_con = j
                    for k in range(j + 1, len(l1[i]) - 1):
                        if l1[i][k] != 'I-content' or k == len(l1[i])-1:
                            endidx1_con = k
                            break
                    if startidx1_con == startidx2_con and endidx1_con == endidx2_con:
                        true_con.append(1)
                    else:
                        true_con.append(0)
                # print(startidx1, endidx1)
    # print(true_con)
    # print(pred_con)

    # source
    accuracy_src = accuracy_score(true_src, pred_src)
    precision_src = precision_score(true_src, pred_src)
    recall_src = recall_score(true_src, pred_src)
    f1_src = f1_score(true_src, pred_src)
    # print(accuracy_src)

    # cue
    accuracy_cue = accuracy_score(true_cue, pred_cue)
    precision_cue = precision_score(true_cue, pred_cue)
    recall_cue = recall_score(true_cue, pred_cue)
    f1_cue = f1_score(true_cue, pred_cue)

    # content
    accuracy_con = accuracy_score(true_con, pred_con)
    precision_con = precision_score(true_con, pred_con)
    recall_con = recall_score(true_con, pred_con)
    f1_con = f1_score(true_con, pred_con)

    return (accuracy_src, precision_src, recall_src, f1_src), (accuracy_cue, precision_cue, recall_cue, f1_cue), (accuracy_con, precision_con, recall_con, f1_con)


def beginOnly(l1, l2):
    true_src = []
    pred_src = []
    true_cue = []
    pred_cue = []
    true_con = []
    pred_con = []

    # source
    for i in range(len(l1)):
        # 正
        for j in range(len(l1[i])):
            if l1[i][j] == 'B-source':
                startidx1 = j
                true_src.append(1)
            # print(startidx1, endidx1)

            if l2[i][j] == 'B-source':
                startidx2 = j
                if startidx1 == startidx2:
                    pred_src.append(1)
                    flag = True  # 设置标志位，如果完全匹配则不用逆向
                else:
                    pred_src.append(0)
                    flag = False
            # print(startidx2, endidx2)

        # 逆
        if not flag:
            for j in range(len(l2[i])):
                if l2[i][j] == 'B-source':
                    startidx2 = j
                    pred_src.append(1)
                # print(startidx2, endidx2)

                if l1[i][j] == 'B-source':
                    startidx1 = j
                    if startidx1 == startidx2:
                        true_src.append(1)
                    else:
                        true_src.append(0)
                # print(startidx1, endidx1)
    # print(true_src)
    # print(pred_src)

    # cue
    for i in range(len(l1)):
        # 正
        for j in range(len(l1[i])):
            if l1[i][j] == 'B-cue':
                startidx1 = j
                true_cue.append(1)
            # print(startidx1, endidx1)

            if l2[i][j] == 'B-cue':
                startidx2 = j
                if startidx1 == startidx2:
                    pred_cue.append(1)
                    flag = True  # 设置标志位，如果完全匹配则不用逆向
                else:
                    pred_cue.append(0)
                    flag = False
            # print(startidx2, endidx2)

        # 逆
        if not flag:
            for j in range(len(l2[i])):
                if l2[i][j] == 'B-cue':
                    startidx2 = j
                    pred_cue.append(1)
                # print(startidx2, endidx2)

                if l1[i][j] == 'B-cue':
                    startidx1 = j
                    if startidx1 == startidx2:
                        true_cue.append(1)
                    else:
                        true_cue.append(0)
                # print(startidx1, endidx1)
    # print(true_cue)
    # print(pred_cue)

    # content
    for i in range(len(l1)):
        # 正
        for j in range(len(l1[i])):
            if l1[i][j] == 'B-content':
                startidx1 = j
                true_con.append(1)
            # print(startidx1, endidx1)

            if l2[i][j] == 'B-content':
                startidx2 = j
                if startidx1 == startidx2:
                    pred_con.append(1)
                    flag = True  # 设置标志位，如果完全匹配则不用逆向
                else:
                    pred_con.append(0)
                    flag = False
            # print(startidx2, endidx2)

        # 逆
        if not flag:
            for j in range(len(l2[i])):
                if l2[i][j] == 'B-content':
                    startidx2 = j
                    pred_con.append(1)
                # print(startidx2, endidx2)

                if l1[i][j] == 'B-content':
                    startidx1 = j
                    if startidx1 == startidx2:
                        true_con.append(1)
                    else:
                        true_con.append(0)
                # print(startidx1, endidx1)
    # print(true_con)
    # print(pred_con)

    # source
    accuracy_src = accuracy_score(true_src, pred_src)
    precision_src = precision_score(true_src, pred_src)
    recall_src = recall_score(true_src, pred_src)
    f1_src = f1_score(true_src, pred_src)
    # print(accuracy_src)

    # cue
    accuracy_cue = accuracy_score(true_cue, pred_cue)
    precision_cue = precision_score(true_cue, pred_cue)
    recall_cue = recall_score(true_cue, pred_cue)
    f1_cue = f1_score(true_cue, pred_cue)

    # content
    accuracy_con = accuracy_score(true_con, pred_con)
    precision_con = precision_score(true_con, pred_con)
    recall_con = recall_score(true_con, pred_con)
    f1_con = f1_score(true_con, pred_con)

    return (accuracy_src, precision_src, recall_src, f1_src), (accuracy_cue, precision_cue, recall_cue, f1_cue), (accuracy_con, precision_con, recall_con, f1_con)


def Jaccard(l1, l2):
    src = []
    cue = []
    con = []

    # source
    for i in range(len(l1)):
        # 正
        for j in range(len(l1[i])):
            if l1[i][j] == 'B-source':
                startidx1src = j
                # print('startidx1={:d}'.format(startidx1))
                for k in range(j + 1, len(l1[i])):
                    # print(l1[i][k])
                    if l1[i][k] != 'I-source' or k == len(l1[i])-1:
                        # print(k)
                        endidx1src = k
                        # print('endidx1={:d}'.format(endidx1))
                        break
                if k == len(l1[i]) - 1:
                    match_rng1_src = [p for p in range(startidx1src, endidx1src+1)]
                else:
                    match_rng1_src = [p for p in range(startidx1src, endidx1src)]
            # print(startidx1, endidx1)

            if l2[i][j] == 'B-source':
                startidx2src = j
                # print('startidx2={:d}'.format(startidx2))
                for k in range(j + 1, len(l2[i]) - 1):
                    if l2[i][k] != 'I-source' or k == len(l1[i]):
                        endidx2src = k
                        # print('endidx2={:d}'.format(endidx2))
                        break
                if k == len(l2[i]) - 1:
                    match_rng2_src = [p for p in range(startidx2src, endidx2src+1)]
                else:
                    match_rng2_src = [p for p in range(startidx2src, endidx2src)]
        # print(match_rng1_src, match_rng2_src)
        a = [val for val in match_rng1_src if val in match_rng2_src]  # 交集
        # a = set(match_rng1).intersection(set(match_rng2))
        # print(float(len(a) / (len(match_rng1) + len(match_rng2) - len(a))))
        if len(match_rng1_src) > 0 or len(match_rng2_src) > 0:
            src.append(float(len(a) / (len(match_rng1_src) + len(match_rng2_src) - len(a))))
        # print(startidx2, endidx2)

    # cue
    for i in range(len(l1)):
        # 正
        # print('startidx1={:d}'.format(startidx1))
        match_rng1_cue = []
        match_rng2_cue = []
        for j in range(len(l1[i])):
            if l1[i][j] == 'B-cue':
                startidx1cue = j
                # print('startidx1={:d}'.format(startidx1))
                for k in range(j + 1, len(l1[i])):
                    # print(l1[i][k])
                    if l1[i][k] != 'I-cue' or k == len(l1[i])-1:
                        endidx1cue = k
                        # print('endidx1={:d}'.format(endidx1))
                        break
                if k == len(l1[i])-1:  # 最后一个元素
                    match_rng1_cue = [p for p in range(startidx1cue, endidx1cue+1)]
                else:
                    match_rng1_cue = [p for p in range(startidx1cue, endidx1cue)]
            # print(startidx1, endidx1)

            # print('startidx2={:d}'.format(startidx2))
            if l2[i][j] == 'B-cue':
                startidx2cue = j
                # print(l2[i][j])
                # print('startidx2={:d}'.format(startidx2))
                for k in range(j + 1, len(l2[i])):
                    # print(l1[i][k])
                    if l2[i][k] != 'I-cue' or k == len(l1[i])-1:
                        endidx2cue = k
                        # print('endidx2={:d}'.format(endidx2))
                        break
                if k == len(l2[i])-1:
                    match_rng2_cue = [p for p in range(startidx2cue, endidx2cue+1)]
                else:
                    match_rng2_cue = [p for p in range(startidx2cue, endidx2cue)]
        # print(match_rng1_cue, match_rng2_cue)
        # a = set(match_rng1).intersection(set(match_rng2))
        a = [val for val in match_rng1_cue if val in match_rng2_cue]  # 交集
        # print(float(len(a) / (len(match_rng1) + len(match_rng2) - len(a))))
        if len(match_rng1_cue) > 0 or len(match_rng2_cue) > 0:
            cue.append(float(len(a) / (len(match_rng1_cue) + len(match_rng2_cue) - len(a))))

    # content
    for i in range(len(l1)):
        # 正
        # print('startidx1={:d}'.format(startidx1))
        match_rng1_con = []
        match_rng2_con = []
        for j in range(len(l1[i])):
            if l1[i][j] == 'B-content':
                startidx1con = j
                # print('startidx1con={:d}'.format(startidx1con))
                for k in range(j + 1, len(l1[i])):
                    # print(l1[i][k])
                    if l1[i][k] != 'I-content' or k == len(l1[i]) - 1:
                        endidx1con = k
                        # print('endidx1con={:d}'.format(endidx1con))
                        break
                if k == len(l1[i])-1:
                    match_rng1_con = [p for p in range(startidx1con, endidx1con + 1)]
                else:
                    match_rng1_con = [p for p in range(startidx1con, endidx1con)]
            # print(startidx1, endidx1)

            # print('startidx2={:d}'.format(startidx2))
            if l2[i][j] == 'B-content':
                startidx2con = j
                # print(l2[i][j])
                # print('startidx2con={:d}'.format(startidx2con))
                for k in range(j + 1, len(l2[i])):
                    # print(l1[i][k])
                    if l2[i][k] != 'I-content' or k == len(l1[i]) - 1:
                        endidx2con = k
                        # print('endidx2con={:d}'.format(endidx2con))
                        break
                if k == len(l2[i])-1:
                    match_rng2_con = [p for p in range(startidx2con, endidx2con+1)]
                else:
                    match_rng2_con = [p for p in range(startidx2con, endidx2con)]
        # print(match_rng1_con, match_rng2_con)
        # a = set(match_rng1).intersection(set(match_rng2))
        a = [val for val in match_rng1_con if val in match_rng2_con]  # 交集
        # print(float(len(a) / (len(match_rng1) + len(match_rng2) - len(a))))
        if len(match_rng1_con) > 0 or len(match_rng2_con) > 0:
            con.append(float(len(a) / (len(match_rng1_con) + len(match_rng2_con) - len(a))))

    # print(src)
    # print(cue)
    # print(con)

    # source
    srcsum = 0
    for ele in range(0, len(src)):
        srcsum += src[ele]
    # print(srcsum)
    jac_src = srcsum / len(src)
    # print(jac_src)

    # cue
    cuesum = 0
    for ele in range(0, len(cue)):
        cuesum += cue[ele]
    jac_cue = cuesum / len(cue)
    # print(jac_cue)

    # content
    consum = 0
    for ele in range(0, len(con)):
        consum += con[ele]
    jac_con = consum / len(con)
    # print(jac_con)

    return jac_src, jac_cue, jac_con

# print(list1)
# print(list2)

print('Strict Matching：\n'
      '(1)source：\nAccuracy = {:.2f}\nPrecision = {:.2f}\nRecall = {:.2f}\nF1_score = {:.2f}\n'
      '(2)cue：\nAccuracy = {:.2f}\nPrecision = {:.2f}\nRecall = {:.2f}\nF1_score = {:.2f}\n'
      '(3)content：\nAccuracy = {:.2f}\nPrecision = {:.2f}\nRecall = {:.2f}\nF1_score = {:.2f}\n'
      .format(strict_matching(list1, list2)[0][0], strict_matching(list1, list2)[0][1], strict_matching(list1, list2)[0][2], strict_matching(list1, list2)[0][3],
              strict_matching(list1, list2)[1][0], strict_matching(list1, list2)[1][1], strict_matching(list1, list2)[1][2], strict_matching(list1, list2)[1][3],
              strict_matching(list1, list2)[2][0], strict_matching(list1, list2)[2][1], strict_matching(list1, list2)[2][2], strict_matching(list1, list2)[2][3]))

print('beginOnly Matching：\n'
      '(1)source：\nAccuracy = {:.2f}\nPrecision = {:.2f}\nRecall = {:.2f}\nF1_score = {:.2f}\n'
      '(2)cue：\nAccuracy = {:.2f}\nPrecision = {:.2f}\nRecall = {:.2f}\nF1_score = {:.2f}\n'
      '(3)content：\nAccuracy = {:.2f}\nPrecision = {:.2f}\nRecall = {:.2f}\nF1_score = {:.2f}\n'
      .format(beginOnly(list1, list2)[0][0], beginOnly(list1, list2)[0][1], beginOnly(list1, list2)[0][2], beginOnly(list1, list2)[0][3],
              beginOnly(list1, list2)[1][0], beginOnly(list1, list2)[1][1], beginOnly(list1, list2)[1][2], beginOnly(list1, list2)[1][3],
              beginOnly(list1, list2)[2][0], beginOnly(list1, list2)[2][1], beginOnly(list1, list2)[2][2], beginOnly(list1, list2)[2][3]))

print('Jaccard Matching：\n'
      '(1)source：\nJaccard Similarity = {:.2f}\n'
      '(2)cue：\nJaccard Similarity = {:.2f}\n'
      '(3)content：\nJaccard Similarity = {:.2f}\n'
      .format(Jaccard(list1, list2)[0], Jaccard(list1, list2)[1], Jaccard(list1, list2)[2]))
