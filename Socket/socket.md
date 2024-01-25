# Socket

Socket, bilgisayar ağlarında veri iletimi için kullanılan bir iletişim aracıdır. Soketler, bilgisayarlar arasında veri alışverişi yapmak için kullanılır ve birçok farklı protokol üzerinde çalışabilirler. En yaygın olarak kullanılan soket türleri, TCP (Transmission Control Protocol) ve UDP (User Datagram Protocol) soketleridir.

Soket programlaması, bilgisayarlar arasında ağ üzerinden veri iletimini sağlamak amacıyla geliştirilen bir programlama paradigmadır. Bu, bir bilgisayarın bir uygulamasının veri göndermesi ve diğer bilgisayarın da bu veriyi alması için bir yol sağlar.

Soket programlaması genellikle şu adımları içerir:

* **Soket Oluşturma:**  İki taraftaki uygulamalar arasında bir bağlantı kurmak için bir soket oluşturulur. Bu, genellikle bir sunucu soketi ve bir istemci soketi içerir.
* **Bağlantı Kurma (Opsiyonel):** Sunucu, istemcilerin bağlanmasını bekler. İstemci, sunucuya bağlanır.
* **Veri Gönderme ve Alma:** Bağlantı kurulduktan sonra, taraflar arasında veri gönderme ve alma işlemi gerçekleşir.
* **Bağlantı Sonlandırma :** İletişim tamamlandığında, soketler kapatılır ve bağlantı sona erer.

Python'da, socket modülü bu tür işlemleri gerçekleştirmek için kullanılır. TCP ve UDP protokollerini destekler ve farklı soket türlerini oluşturmanıza, bağlantıları yönetmenize ve veri alışverişi yapmanıza olanak tanır.