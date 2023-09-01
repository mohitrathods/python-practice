# class MyClass:
#     def __init__(self):
#         self.x = 10
#         print(lambda self:self)
#
#     # def perform_operation(self, y):
#     #     # Define a lambda function that adds x and y
#     #     add_lambda = lambda a: a + self.x
#     #
#     #     # Use the lambda function
#     #     result = add_lambda(y)
#     #     return result
#
# obj = MyClass()
# import datetime
# str_time = '2023-08-10T10:14:04'
# str_time1 = '2023-08-10T11:38:00'
# d = datetime.datetime.strptime(str_time, "%Y-%m-%dT%H:%M:%S")
# d1 = datetime.datetime.strptime(str_time1, "%Y-%m-%dT%H:%M:%S")
# print(d1-d) # results 1:23:56
# print((d1-d).seconds)
# today = datetime.date.today()
# print(type(today),type(d))

list_of_properties = """Sewer Pump Houses in Varanasi City
Sewer Manholes in Varanasi City
Sewer Lines in Varanasi City
Scour Valves in Varanasi City
Rivers in Varanasi City
Religious Structures in Varanasi City
Raw Water Pipe Lines in Varanasi City
Railway Lines in Varanasi City
Ponds Kunds in Varanasi City
Park Gardens in Varanasi City
Water Reservoirs in Varanasi City
Traffic Signal Posts in Varanasi City
Zone Boundary in Varanasi City
Tube Wells in Varanasi City
Water ATMs in Varanasi City
Ward Boundary in Varanasi City
Waste to Compost Plants in Varanasi City
Water Supply Network in Varanasi City"""

l1 = list_of_properties.split('\n')
print(l1)
l2 = list(map(lambda i : i[:-5],l1))
print(l2)