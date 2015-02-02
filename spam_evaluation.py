import sys

def tfpn(label,pred):
    if pred == 'SPAM':
        if label == 'SPAM':
            return 'tp'
        else:
            return 'fp'
    else:
        if label == 'SPAM':
            return 'fn'
        else:
            return 'tn'

def main():
    labelfile = open(sys.argv[1])
    predfile = open(sys.argv[2])
    
    labels = [line.strip() for line in labelfile]
    preds = [line.strip() for line in predfile]

    labelfile.close()
    predfile.close()

    tfpns = [tfpn(labels[i], preds[i]) for i in range(len(labels))]
    tps = tfpns.count('tp')
    fps = tfpns.count('fp')
    fns = tfpns.count('fn')
    tns = tfpns.count('tn')

    accu = (tps + tns) / len(tfpns)
    spamrecall = tps / (tps + fns)
    spamprecision = tps / (tps + fps)
    spamf1 = (2*tps) / (2*tps + fps + fns)
    hamrecall = tns / (tns + fps)
    hamprecision = tns / (tns + fns)
    hamf1 = (2*tns) / (2*tns + fps + fns)

    print('tps: ' + str(tps))
    print('fps: ' + str(fps))
    print('fns: ' + str(fns))
    print('tns: ' + str(tns))
    print('accu: ' + str(accu))
    print('spamrecall: ' + str(spamrecall))
    print('spamprecision: ' + str(spamprecision))
    print('spamf1: ' + str(spamf1))
    print('hamrecall: ' + str(hamrecall))
    print('hamprecision: ' + str(hamprecision))
    print('hamf1: ' + str(hamf1))

if __name__ == '__main__':
    main()
