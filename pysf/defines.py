# -*- encoding: utf-8 -*-
""" defines.py は C 言語での define マクロの変わりに使います。defines.py はアプリケーション毎に異なります。C 言語でコンパイラから -D"..." のようにマクロ文字列を与えられないので、def.py に書き込むことで代用します

    幾つかのマクロも python 変数として定義します。-D parameter で何時でも変更可能とします。
オプション バラメータ:lstDfntnStt には os.arg から -D で与えられたパラメータ群を設定します。

""" 
