from lilaclib import *

def pre_build():
    #aur_pre_build()
    #if _G.newver is not None and _G.newver != _G.oldver:
    #    update_pkgver_and_pkgrel(_G.newver)
    #else:
    #    raise Exception("new version check failed (new ver is None)")

def post_build():
    aur_post_build()
    update_aur_repo()
