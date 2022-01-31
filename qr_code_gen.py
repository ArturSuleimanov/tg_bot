import qrcode

class Counter:      #amount of codes during one session
    counter = 0

def qr_code_generator(link):
    '''
    Function takes link and saves QR code for this link
    :param link: The link you need to convert to QRcode
    :return: file name
    '''
    image = qrcode.make(link)
    file_name = f'{Counter.counter}.jpg'
    image.save(file_name)
    Counter.counter += 1
    return file_name





if __name__ == '__main__':    # test of qr_code_generator function
    print(type(qr_code_generator('https://yandex.ru')))
