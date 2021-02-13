from lilaclib import edit_file

def pre_build():
    for line in edit_file('PKGBUILD'):
        if line.startswith('pkgname='):
            print('pkgname=cgproxy-gapoon-git')
        print(line)
        print('''
        prepare(){
            cd ${srcdir}/${pkgname}
            git fetch origin pull/29/head:huyz-pr
            git merge --no-commit huyz-pr
        }''')
