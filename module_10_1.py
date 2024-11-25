import threading
from datetime import datetime
from time import sleep


def write_words(word_count, file_name):  # количество записываемых слов / название файла, куда будут записываться слова.
    with open(file_name, 'w', encoding='utf-8') as f:
        for i in range(word_count):
            f.write(f"Какое-то слово № {i + 1}\n")
            sleep(0.1)  # прерывание после записи
        print(f"Завершилась запись в файл {file_name}")


start_time1 = datetime.now()

write_words(10, 'example1.txt')
write_words(30, 'example2.txt')
write_words(200, 'example3.txt')
write_words(100, 'example4.txt')

end_time1 = datetime.now()
print(f'Работа потоков {end_time1 - start_time1}')

start_time2 = datetime.now()

thread_1 = threading.Thread(target=write_words, args=(10, 'example5.txt'))
thread_2 = threading.Thread(target=write_words, args=(30, 'example6.txt'))
thread_3 = threading.Thread(target=write_words, args=(200, 'example7.txt'))
thread_4 = threading.Thread(target=write_words, args=(100, 'example8.txt'))

thread_1.start()
thread_2.start()
thread_3.start()
thread_4.start()

thread_1.join()
thread_2.join()
thread_3.join()
thread_4.join()

end_time2 = datetime.now()
print(f'Работа потоков {end_time2 - start_time2}')
