from factory.mysql_factory import MySqlFactory

usecase = MySqlFactory.create()
response = usecase.do_something(True)
print(response)