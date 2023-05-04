from flask import Flask, render_template, request, redirect, url_for
import user
import counter

# 定位目前載入資料夾的位置
app = Flask(__name__)
# ----- ----- ----- ----- -----
# 一般使用
# ----- ----- ----- ----- -----

# 轉入後續任何頁面的起始頁面。
@app.route('/')
def get_home_page():
    return render_template('home_page.html')

# ----- ----- ----- ----- -----
# 內部使用
# ----- ----- ----- ----- -----

# 櫃檯人員進行登入時的預設頁面。
@app.route('/login', methods=["POST", "GET"])
def get_login_page():
    if request.method == 'POST':
        login_data = {
            'user_id': request.form['accountInput'],
            'pwd': request.form['passwordInput'],
            'counter_id': request.form['counterNumberSelect']
        }

        if user.user_login(login_data['user_id'], login_data['pwd']):
            print('User {} login success.'. format(login_data['user_id']))
            return redirect(
                url_for(
                    'get_panel_page',
                    user_id=login_data['user_id'],
                    counter_id=login_data['counter_id']
                )
            )

        else:
            print('User {} login fail.'. format(login_data['user_id']))
            return render_template('login_page.html', max_counter_number=counter.get_max_counter_number(), msg='登入失敗！您所輸入的帳號或是密碼有誤，請重新確認後再嘗試。')

    else:
        return render_template('login_page.html', max_counter_number=counter.get_max_counter_number())

# 櫃臺人員完成登入後，轉入的操作頁面。
@app.route('/panel/<user_id>/<counter_id>')
def get_panel_page(user_id, counter_id):
    return render_template('panel_page.html', user_id=user_id, counter_id=counter_id)

# ----- ----- ----- ----- -----
# 外部使用
# ----- ----- ----- ----- -----

# 轉入 `/counter/<counter_id>` 的前置頁面，於此頁面中決定要顯示的 `counter_id`。
@app.route('/counter', methods=["POST", "GET"])
def get_counter_select_page():
    if request.method == 'POST':
        counter_id = request.form['counterId']

        print('Counter {} display.'. format(counter_id))
        return redirect(
            url_for(
                'get_counter_display_page',
                counter_id=counter_id,
            )
        )

    else:
        return render_template('counter_select_page.html', max_counter_number=counter.get_max_counter_number())

# 顯示對應 `counter_id` 目前的叫號號碼。
@app.route('/counter/<counter_id>')
def get_counter_display_page(counter_id):
    return render_template('counter_display_page.html', counter_id=counter_id)

# 顯示目前等候人數，並提供按鈕供外部人員領取排隊用票。
@app.route('/ticket-machine')
def get_ticket_machine_page():
    return render_template('ticket_machine_page.html')
