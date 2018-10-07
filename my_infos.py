import user_info
"""调用用户的类的整个模块"""

m_info=user_info.User_info('z','x','male','26')
m_info.describe_user()
m_info.greet_user()
m_info.increment_login_attempts()
m_info.increment_login_attempts()
m_info.reset_login_attempts()
print(m_info.login_attempts)


zx=user_info.Admin('z','x','male',26)
"""调用管理员的类"""
zx.describe_user()
zx.privileges.show_priviledges()