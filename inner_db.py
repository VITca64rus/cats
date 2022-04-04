import os
from werkzeug.security import generate_password_hash
from sber.models import User, Cat
from sber import db


def inner():
    data = []
    admin = User.query.filter_by(login=os.environ['PASSWORD_DB']).first()
    if admin is None:
        admin = User(login=os.environ['USER_DB'], password=generate_password_hash(os.environ['PASSWORD_DB']))
        db.session.add(admin)
        db.session.commit()
    data.append(Cat(name='Мартин', age='8', breed='Мэйн-кун', info='Красивый мальчик',
                    photo='https://static.lolkot.ru/images/user-albums/38210/foto13343.jpg'))
    data.append(Cat(name='Крис', age='5', breed='Мэйн-кун', info='Прекрасная девочка',
                    photo='https://st2.depositphotos.com/2166845/11860/i/450/depositphotos_118600596-stock-photo-purebred-maine-coon-cat-isolated.jpg'))
    data.append(Cat(name='Соня', age='3', breed='Британская', info='Серая девочка',
                    photo='https://avatars.mds.yandex.net/get-pdb/2441435/d9241e50-3ef7-4623-897d-4118e21c9fd5/s1200?webp=false'))
    data.append(Cat(name='Саймон', age='4', breed='Британская', info='Пушистый мальчик',
                    photo='https://mtdata.ru/u8/photo28BC/20706972412-0/original.jpg'))
    data.append(Cat(name='Цунами', age='10', breed='Персидская', info='Добрейший ангелок',
                    photo='http://todofondos.com/bin/fondos/03/77/64d.jpg'))
    data.append(Cat(name='Атос', age='15', breed='Персидская', info='Тусовый парень',
                    photo='https://porodakoshki.ru/wp-content/uploads/2018/10/Persidskaya-koshka-lezhit-e1539016050247.jpg'))
    data.append(Cat(name='Наоми', age='10', breed='Сиамская', info='Девочка добрая',
                    photo='https://avatars.mds.yandex.net/i?id=b6c1941a7b919f056152793ab2093663-5480599-images-thumbs&n=13'))
    data.append(Cat(name='Альбус', age='9', breed='Сиамская', info='Славный мальчик',
                    photo='https://kot-koshka.ru/wp-content/uploads/2015/10/siamskie-koshki-foto-16.jpg'))
    data.append(Cat(name='Рокки', age='8', breed='Манчкин', info='Славный мальчик',
                    photo='https://lamu-vet.org/img/hvos-2021/5277/image_iga4wOYCPuhll.jpg'))
    data.append(Cat(name='Ворсинка', age='8', breed='Манчкин', info='Славный мальчик',
                    photo='https://avatars.mds.yandex.net/i?id=7f9c7d7029a6ad0c43101fd21971c180-5644622-images-thumbs&n=13'))
    data.append(Cat(name='Серсея', age='3', breed='Рэгдолл', info='Славная девочка',
                    photo='https://petskb.com/wp-content/uploads/2020/04/Ragdoll-closeup-face.jpg'))
    data.append(Cat(name='Зорро', age='4', breed='Рэгдолл', info='Славный кот',
                    photo='https://cats-world.ru/wp-content/uploads/2017/02/ryegdoll1-e1439814715774.jpeg'))
    data.append(Cat(name='Амели', age='2', breed='Бенгальская', info='Славный кот',
                    photo='https://avatars.mds.yandex.net/get-pdb/805781/23a60863-cc4a-42f0-8451-993b3fd598a1/s600?webp=false'))
    data.append(Cat(name='Фокси', age='5', breed='Бенгальская', info='Славный кот',
                    photo='https://uc.lolkot.ru/picture/51246-38210-1.jpg'))
    data.append(Cat(name='Гризли', age='4', breed='Сибирская', info='Славный кот',
                    photo='https://gafki.ru/wp-content/uploads/2019/10/kartinka-4.-sibirskaja-koshka.jpg'))
    data.append(Cat(name='Дымка', age='4', breed='Сибирская', info='Славный кошка',
                    photo='http://animals-portal.ru/wp-content/uploads/2018/01/gfhf6575.jpg'))
    data.append(Cat(name='Табби', age='1', breed='Шотладская вислоухая', info='Славный кот',
                   photo='https://vivarating.ru/wp-content/uploads/2022/02/pp_image_18339_1yx8dj1gptshot1.jpg'))
    data.append(Cat(name='Тень', age='5', breed='Шотладская вислоухая', info='Славный кот',
                    photo='https://usatik.ru/wp-content/uploads/2019/10/shotlandskaya-vislouhaya-koshka-obl.jpg'))
    data.append(Cat(name='Браунни', age='2', breed='Шотладская вислоухая', info='Славный кот',
                    photo='https://img.unibo.ru/foto/message_fotos/6073/60737538/foto_largest.jpg'))
    data.append(Cat(name='Пинки', age='2', breed='Ангорская', info='Славный кот',
                    photo='https://porodakoshki.ru/wp-content/uploads/2018/10/Tureckaya-angora-cena-e1540030429602.jpg'))
    data.append(Cat(name='Снежок', age='2', breed='Ангорская', info='Славный кот',
                    photo='https://legkovmeste.ru/wp-content/uploads/2019/02/post_5b0d4c020358f-600x400.jpg'))

    for i in data:
        cat = Cat.query.filter_by(name=i.name, photo=i.photo, age=i.age,
                                  breed=i.breed, info=i.info).first()
        if cat is None:
            db.session.add(i)
            db.session.commit()
