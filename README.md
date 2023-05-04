# 概述
這是個人學習與練習所使用的 Repo，主要目標為透過 Flask 製作基於 Web 架構所構成的叫號系統。

# 構成
- 一般使用
    - `/` : 轉入後續任何頁面的起始頁面。
- 內部使用
    - `/login` : 櫃臺人員進行登入時的預設頁面。
    - `/panel/<user_id>/<counter_id>` : 櫃臺人員完成登入後，轉入的操作頁面。
- 外部使用
    - `/counter` : 轉入 `/counter/<counter_id>` 的前置頁面，於此頁面中決定要顯示的 `counter_id`。
    - `/counter/<counter_id>` : 顯示對應 `counter_id` 目前的叫號號碼。
    - `/ticket-machine` : 顯示目前等候人數，並提供按鈕供外部人員領取排隊用票。
- `` : 。
- `` : 。

# 重點筆記
## url_for
在編寫登入功能的時候，發現登入成功後要轉入 `panel` 頁面的時候，始終會出現以下錯誤：
```
werkzeug.routing.exceptions.BuildError: Could not build url for endpoint 'panel' with values ['counter_id', 'user_id']. Did you mean 'get_panel_page' instead?
```
比對了一下過去 `url_for` 成功的段落，但明明都長得差不多卻一邊成功、一邊失敗，上網找了幾篇文章但跟我的狀況有點落差，而排除不了問題…… 不過實際上這段錯誤就有提到解法，但沒有意識過來。最終找到「[參考資料 [3]](https://blog.csdn.net/yannanxiu/article/details/52287870)」，得知 `url_for` 的第一個參數並不是設置 `@app.route` 的路徑，而是要寫入 `函數名稱`。

在編寫的時候，我誤以為 `url_for` 是要填入路徑，而設為 `url_for('panel', ... )`，另一方面，監聽的路徑與函數的命名沒有設置相同：
```
@app.route('/panel/<user_id>/<counter_id>')
def get_panel_page(user_id, counter_id):
    return render_template('panel_page.html')
```
這使得 `url_for` 一直跳出錯誤，而排除方法也僅僅只要按照錯誤訊息的提示，使用 `get_panel_page` 取代即可：
```
url_for('get_panel_page', ... )
```

# 使用項目
- [Python](https://www.python.org/)
    - [Flask](https://flask.palletsprojects.com/en/2.3.x/)
    - [Flask-RESTful](https://flask-restful.readthedocs.io/en/latest/)
- [Draw.io (Diagrams.net)](https://app.diagrams.net/)
- [Tiger icons created by Freepik - Flaticon](https://www.flaticon.com/free-icons/tiger)

# 參考資料
1. [How to set vertical alignment in Bootstrap ? - GeeksforGeeks](https://www.geeksforgeeks.org/how-to-set-vertical-alignment-in-bootstrap/)
2. [Python Web Flask — 如何透過Form取得資料. 使用POST方式並且使用session，來製作login與logout功能。 | Python Everywhere -from Beginner to Advanced](https://medium.com/seaniap/python-web-flask-%E5%A6%82%E4%BD%95%E9%80%8F%E9%81%8Eform%E5%8F%96%E5%BE%97%E8%B3%87%E6%96%99-7a63ebf9ff1f)
3. [【Flask】Flask中关于url_for()的坑_url_for在web前端引用不了_阏男秀的博客-CSDN博客](https://blog.csdn.net/yannanxiu/article/details/52287870)
4. [Python Web Flask — Flask-RESTful簡易CRUD API製作 | by Sean Yeh | Python Everywhere -from Beginner to Advanced | Medium](https://medium.com/seaniap/python-web-flask-flask-restful%E7%B0%A1%E6%98%93crud-api%E8%A3%BD%E4%BD%9C-1a4023c1b768)


# 更新摘要
1. 2023-05-02 : 建立 Repo。
2. 2023-05-03 : 製作。
    - 完成部分頁面的基礎顯示與導向。
3. 2023-05-04 : 製作。
    - 完成所有頁面的基礎顯示與導向。
    - 製作局部函數功能。
4. 123

# 雜談
此段落是記錄我自己雜七雜八的思考，簡單來說就是廢話。
- 2023-05-03
    - 腦袋卡住的時候真的要停一下再來想，`url_for` 那邊明明是個很簡單的小問題，甚至錯誤訊息中都有提示，結果卡了好一段時間 xD
