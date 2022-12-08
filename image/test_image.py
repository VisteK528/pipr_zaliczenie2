from image import Image


def test__str__():
    data = [
         (0, 1, 122), (0, 2, 21), (1, 1, 112),
         (1, 2, 30), (2, 0, 11), (2, 1, 44),
         (2, 2, 31)]
    result = "0 122 21 \n0 112 30 \n11 44 31 \n"
    image = Image(3, 3, data)
    assert str(image) == result


def test_negative():
    data = [(0, 0, 255), (0, 1, 144), (1, 1, 55)]
    image = Image(2, 2, data)
    result = "255 144 \n0 55 \n"
    assert str(image) == result
    negative_image = image.negative()
    negative_result = "0 111 \n255 200 \n"
    assert str(negative_image) == negative_result
    assert str(image) == result


def test_add_two_images():
    data = [(0, 0, 200), (0, 1, 144), (1, 1, 55)]
    data2 = [(0, 0, 55), (1, 0, 40)]
    image = Image(2, 2, data)
    image2 = Image(2, 2, data2)
    result = "255 144 \n40 55 \n"
    image3 = image + image2
    assert str(image3) == result


def test_add_empty_image():
    data = [(0, 0, 200), (0, 1, 144), (1, 1, 55)]
    image = Image(2, 2, data)
    image2 = Image(2, 2)
    result = "200 144 \n0 55 \n"
    image3 = image + image2
    assert str(image3) == result
