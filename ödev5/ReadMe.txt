Pytest, Python dilinde bir test çerçevesidir. Pytest, test senaryolarını tanımlamak ve yürütmek için çeşitli araçlar sağlar. Pytest ayrıca, testlerin otomatik olarak yürütülmesine ve sonuçların otomatik olarak değerlendirilmesine yardımcı olacak özellikler içerir.

Pytest'in en önemli özelliklerinden biri, kullanıcının testlerini işaretlemesine ve bu testleri daha sonra yürütme veya atlamayı sağlayan dekoratörler sunmasıdır. Pytest, bir testin koşullarını belirleyen bu dekoratörlerle birlikte kullanıldığında daha esnek ve özelleştirilebilir hale gelir.

Pytest'de sık kullanılan bazı dekoratörler:

@pytest.fixture: Bu dekoratör, test fonksiyonlarına eklenerek, testlerin ihtiyaç duyduğu verileri, nesneleri ve diğer kaynakları sağlar. Fixture'lar, testlerin bir parçası olarak çalışan nesnelerdir.

@pytest.mark.parametrize: Bu dekoratör, test fonksiyonlarına eklenerek, bir veya daha fazla parametreyle çalışacak test senaryolarının listesini sağlar. Bu dekoratör, test senaryolarının tekrar kullanılmasını ve daha az kod yazılmasını sağlar.

@pytest.mark.skip: Bu dekoratör, test fonksiyonlarını atlamak için kullanılır. Bu, test senaryolarının bazı koşullar altında çalıştırılmamasını sağlar.

@pytest.mark.xfail: Bu dekoratör, bir testin özellikle başarısız olacağını bilerek kullanılır. Bu, bir testin hatalı sonuç vermesini bekleyen durumlarda kullanılır.

@pytest.mark.timeout: Bu dekoratör, belirli bir süre içinde tamamlanması gereken testler için kullanılır. Bu, test süresinin sınırlanması gerektiği durumlarda kullanılabilir.

@pytest.mark.dependency: Bu dekoratör, testler arasında bağımlılıklar tanımlamanıza olanak tanır. Bu, bir testin diğer bir testin başarılı bir şekilde çalışması için önce çalışması gerektiği durumlarda kullanılabilir.

Bu dekoratörler, Pytest testlerini daha esnek ve özelleştirilebilir hale getirmenize olanak tanır. 