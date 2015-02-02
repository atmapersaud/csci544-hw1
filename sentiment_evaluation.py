import sys

def tfpn(label,pred):
    if pred == 'POS':
        if label == 'POS':
            return 'tp'
        else:
            return 'fp'
    else:
        if label == 'POS':
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
    posrecall = tps / (tps + fns)
    posprecision = tps / (tps + fps)
    posf1 = (2*tps) / (2*tps + fps + fns)
    negrecall = tns / (tns + fps)
    negprecision = tns / (tns + fns)
    negf1 = (2*tns) / (2*tns + fps + fns)

    print('tps: ' + str(tps))
    print('fps: ' + str(fps))
    print('fns: ' + str(fns))
    print('tns: ' + str(tns))
    print('accu: ' + str(accu))
    print('posrecall: ' + str(posrecall))
    print('posprecision: ' + str(posprecision))
    print('posf1: ' + str(posf1))
    print('negrecall: ' + str(negrecall))
    print('negprecision: ' + str(negprecision))
    print('negf1: ' + str(negf1))

if __name__ == '__main__':
    main()
