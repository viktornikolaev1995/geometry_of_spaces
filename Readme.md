# Geometry of spaces

## Описание
gbXML файл с геометрией здания и файл объектов внутри здания можно получить из Revit 
c помощью скрипта Dynamo `upload_geometry.dyn`:

![dynamo_script](https://github.com/viktornikolaev1995/geometry_of_spaces/blob/test/images/photo_2022-12-28_13-12-03.jpg "dynamo_script") 

На рисунке ниже продемонстрирована выгрузка геометрии пространств:
![geometry_spaces](https://github.com/viktornikolaev1995/geometry_of_spaces/blob/test/images/photo_2022-12-28_13-45-42.jpg "geometry_spaces") 

На рисунке ниже продемонстрирована выгрузка геометрии выбранных элементов внутри здания:
![elements_locations](https://github.com/viktornikolaev1995/geometry_of_spaces/blob/test/images/photo_2022-12-28_13-45-41.jpg "elements_locations") 

Геометрия элементов выгружается в виде 2 точек, минимальной и максимальной, взятых по BoundingBox элемента, для последующих представлений в визуализации. 
Наименование и геометрия элементов сохраняются в формате csv.

Посредством Dynamo Player можно вносить корректировки в программу, выбирать необходимые элементы, указывать пути сохранения gbXML с геометрией пространств и csv файла с геометрией элементов

![script_with_dynamo_player](https://github.com/viktornikolaev1995/geometry_of_spaces/blob/test/images/photo_2022-12-28_20-15-15.jpg "script_with_dynamo_player") 

После получения файлов с геометриями, можно получить их визуализацию:
![geometry_visualization](https://github.com/viktornikolaev1995/geometry_of_spaces/blob/test/images/figure.png "geometry_visualization") 

Для этого необходимо установить зависимости, находящиеся в файле requirements.txt:
`pip install -r requirements.txt`

Либо, если установлена poetry:

`poetry shell` и `poetry install`

Далее передать требуемые аргументы в функции render_objects и получить визуализацию геометрии.
