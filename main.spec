# -*- mode: python ; coding: utf-8 -*-

block_cipher = None


a = Analysis(['main.py'],
             pathex=['C:\\Users\\rollm\\Desktop\\Numerical Methods Project - 3'],
             binaries=[],
             datas=[('C:\\Program Files (x86)\\Python38-32\\Lib\\site-packages\\sklearn\\.libs\\vcomp140.dll', '.')],
             hiddenimports=['numpy', 'scikit-learn', 'sklearn.utils._cython_blas', 'matplotlib'],
             hookspath=[],
             runtime_hooks=[],
             excludes=[],
             win_no_prefer_redirects=False,
             win_private_assemblies=False,
             cipher=block_cipher,
             noarchive=False)
pyz = PYZ(a.pure, a.zipped_data,
             cipher=block_cipher)
exe = EXE(pyz,
          a.scripts,
          a.binaries,
          a.zipfiles,
          a.datas,
          [],
          name='main',
          debug=False,
          bootloader_ignore_signals=False,
          strip=False,
          upx=True,
          upx_exclude=[],
          runtime_tmpdir=None,
          console=False )
