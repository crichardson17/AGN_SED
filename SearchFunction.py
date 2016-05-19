import sys, os
listonly = False
textexts = ['.lin', '.txt','.py']

def searcher(startdir,searchkey):
    global fcount, vcount
    fcount=vcount=0
    for (thisDir, dirsHere, filesHere) in os.walk(startdir):
        for fname in filesHere:
            fpath=os.path.join(thisDir, fname)
            print(fpath)
            visitfile(fpath,searchkey)
def visitfile(fpath,searchkey):
    global fcount,vcount
    print(vcount+1, '=>', fpath)
    try:
        if not listonly:
            if os.path.splitext(fpath)[1] not in textexts:
                print('Skipping', fpath)
            elif searchkey in open(fpath).read():
                input('%s has %s' % (fpath,searchkey))
                fcount+=1
    except:
        print('Failed:', fpath, sys.exc_info()[0])
    vcount += 1


searcher('/Users/compastro/greene/AGN_SED/', ".lin")
