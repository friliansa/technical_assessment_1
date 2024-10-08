try:
    # Inputan jumlah bilangan deret yang akan ditampilkan, dilanjutkan mengkonversi inputan menjadi integer
    n = int(input('Masukkan jumlah deret bilangan aritmatika: ')) 

    # Deklarasi Nilai awal deret atau suku ke-1 dan Perbedaan nilai antar suku
    init = 2
    diff = 3

    # Menampilkan deret aritmatika
    print('Deret bilangan aritmatika: ', end='') 
    for i in range(n):
        # Mencari nilai dari bilangan deret pada suku ke-i
        bil = init + (diff*i)
        if i<(n-1):
            # Menampilkan ',' setelah bilangan apabila i bukan suku terakhir
            print(bil, end=",")
        else:
            # Hanya menampilkan bilangan apabila i suku terakhir
            print(bil, end="")
except:
    # Apabila user memasukkan selain bilangan > 0
    print('Inputan harus berupa bilangan dan bernilai > 0.')