import csv

import numpy as np
import xgbxml
from lxml import etree
from matplotlib import pyplot as plt
from mpl_toolkits.mplot3d.art3d import Poly3DCollection
from pydantic import parse_obj_as


def processed_points(min_point: tuple[int | float], max_point: tuple[int | float]):
    min_point = (min_point[0] / 1000, min_point[1] / 1000, min_point[2] / 1000)  # type: ignore
    max_point = (max_point[0] / 1000, max_point[1] / 1000, max_point[2] / 1000)  # type: ignore
    return min_point, max_point


def find_all_points_by_min_and_max(min_point: tuple[float], max_point: tuple[float]):
    return [
        min_point,
        (max_point[0], min_point[1], min_point[2]),  # type: ignore
        (max_point[0], max_point[1], min_point[2]),  # type: ignore
        (min_point[0], max_point[1], min_point[2]),  # type: ignore
        (min_point[0], min_point[1], max_point[2]),  # type: ignore
        (max_point[0], min_point[1], max_point[2]),  # type: ignore
        max_point,
        (min_point[0], max_point[1], max_point[2]),  # type: ignore
    ]


def add_object(
    ax: "Axes3DSubplot",  # type: ignore # noqa: F821
    name: str,
    min_point: tuple[int | float],
    max_point: tuple[int | float],
) -> None:
    """
    :param ax: Axes3DSubplot
    :param name: name of element
    :param min_point: min point of boundary box
    :param max_point: max point of boundary box
    :return: None
    """
    min_point, max_point = processed_points(min_point, max_point)
    points = np.array(find_all_points_by_min_and_max(min_point, max_point))
    verts = [
        [points[0], points[1], points[2], points[3]],
        [points[4], points[5], points[6], points[7]],
        [points[0], points[1], points[5], points[4]],
        [points[2], points[3], points[7], points[6]],
        [points[1], points[2], points[6], points[5]],
        [points[4], points[7], points[3], points[0]],
    ]
    ax.add_collection3d(Poly3DCollection(verts, facecolors="cyan", linewidths=1, edgecolors="r", alpha=0.20))
    ax.text(max_point[0], max_point[1], max_point[2], name, color="red")  # type: ignore


def processed_csv_file(filepath: str, delimiter: str = ",") -> list[dict]:
    with open(filepath) as csvfile:
        reader = csv.DictReader(csvfile, delimiter=delimiter)
        return [element for element in reader]


def render_objects(
    gbxml_filepath: str,
    csv_filepath: str,
    title: str,
    picture_filename: str,
    is_show_render: bool = False,
) -> None:
    """
    Renders 3d objects
    :param gbxml_filepath: gbXML file path, i.e. r'/home/gbxml.xml' to render geometry of spaces
    :param csv_filepath: csv file path i.e. r'/home/elements.csv' to render selected elements
    :param title: render title
    :param picture_filename: filename of saved figure
    :param is_show_render: is show render of objects or not?
    :return: None
    """
    parser = xgbxml.get_parser("0.37")
    tree = etree.parse(gbxml_filepath, parser)
    gbxml = tree.getroot()
    ax = gbxml.Campus.render()
    ax.set_xlabel("X axis")
    ax.set_ylabel("Y axis")
    ax.set_zlabel("Z axis")
    elements = processed_csv_file(csv_filepath)
    for element in elements:
        add_object(
            ax,
            element["Name"],
            (float(element["MinX"]), float(element["MinY"]), float(element["MinZ"])),  # type: ignore
            (float(element["MaxX"]), float(element["MaxY"]), float(element["MaxZ"])),  # type: ignore
        )
    plt.title(title)
    plt.savefig(picture_filename)
    if is_show_render:
        plt.show()


if __name__ == "__main__":
    gbxml_filepath = input(
        "Введите путь до gbXML файла (к примеру: ./docs/test.xml): "
    )
    csv_filepath = input(
        "Введите путь до csv файла (к примеру: ./docs/test.csv): "
    )
    title = input("Введите подпись к рендеру объектов (к примеру: Test_BIM_FDS): ")
    picture_filename = input("Введите наименование сохраненной картинки рендера (к примеру: figure): ")
    is_show_render = parse_obj_as(bool, input("Нужно ли показывать рендер? (True/False): "))

    render_objects(
        gbxml_filepath=gbxml_filepath,
        csv_filepath=csv_filepath,
        title=title,
        picture_filename=picture_filename,
        is_show_render=is_show_render,
    )
