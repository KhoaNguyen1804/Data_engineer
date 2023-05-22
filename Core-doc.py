# Python cơ bản 1
"""
1. Kiểu dữ liệu
    - Các kiểu dữ liệu trong python: int, float, bool, str,
                        list, tuple, set, dict, None, Module
    a. Kiểu int:
        - Là các số có dạng: 1, 2, 3, ...
        - Để ép kiểu dữ liệu về dạng int thì ta dùng câu lệnh:
            int(x): với x là dữ liệu cần ép kiểu
    b. Kiểu float:
        - Là các số có dạng: 1.1, 1.2, 1.3, ...
        - Để ép kiểu dữ liệu về dạng float thì ta dùng câu lệnh:
            float(x): với x là dữ liệu cần ép kiểu
    c. Math function:
        - Là hàm tính toán số học:
        - Có các thuộc tính tiêu biểu sau:
            math.ceil(x): làm tròn số x lên thành số nguyên gần nhất
            math.floor(x): làm tròn số x xuống thành số nguyên gần nhất
            math.sqrt(x): trả về căn bậc hai của số x
            math.exp(x): trả về giá trị của hàm số mũ ex
            math.log(x[, base]): trả về logarit tự nhiên (base e) của số x, hoặc logarit cơ số base của x
                nếu base được chỉ định
            math.sin(x): trả về giá trị của hàm sin(x)
            math.cos(x): trả về giá trị của hàm cos(x)
            math.tan(x): trả về giá trị của hàm tan(x)
            math.degrees(x): chuyển đổi góc x từ radian sang độ
            math.radians(x): chuyển đổi góc x từ độ sang radian
    d. Kiểu bin:
        - Là biểu diễn cho kiểu số nhị phân
        - VD: bin(9) = 0b1001 trong đó
            0b: biểu thị cho việc đây là một số nhị phân
    e. Kiểu complex:
        - Là biểu diễn cho kiểu số phức
        - VD: complex(3, 4) = 3+4j
    f. Kiểu boolean
        - Là kiểu biểu diễn cho giá trị đúng hoặc sai
        - Để ép kiểu sang dạng boolean ta dùng: bool(x) - trong đó x là giá trị cần ép kiểu

2. Toán tử
    - Các phép toán trong kiểu số học:
        Addition: phép cộng (+)
        Subtraction: phép trừ (-)
        Multiplication: phép nhân (*)
        Division: phép chia (/)
        Modulo: phép chia lấy dư (%)
        Exponentiation: phép lũy thừa (**)
        Floor division: phép chia lấy phần nguyên. (//)
    - Toán tử gán: +=, -=, /=, *=

3. Biến - Hằng
    - Biến được dùng để lưu trữ dữ liệu
            VD: a = 5
    - Trong python không có khái niệm hằng số nhưng ta cũng có thể
        quy định hằng số được khai báo bằng tất cả các chữ hoa
            VD: PI = 3.14

4. String
    - String là biến có thể được lưu trữ dạng text
        VD: str = 'QuangND'
    - Có thể dùng dấu: '', "" hoặc để xuống dòng trong string ta có thể dùng ''' text '''
    - Nối 2 string bằng dấu +
    - Ép kiểu sang string chúng ta dùng hàm str()
        VD: str(100) = 100 (string)
    - Sử dụng " hay ' trong string ta sử dụng như sau: \", \', ..
    - Không thể thay thế một từ trong string nhưng có thể thêm chữ vào đằng sau nó
        VD:
            str = "Tôi học Python"
            print(str+' 3')
            => Tôi học Python 3
    a. Kiểu viết string
        - thêm f vào trước string
        VD:
            name = "Quang"
            age = 27
            print(f'Name: {name}, age: {age}')

        - thêm .format vào đằng sau string đó
        VD:
            name = "Quang"
            age = 27
            print('Name: {0}, age: {1}'.format(name, age))
        VD:
            print('Name: {name}, age: {age}'.format(name='Quang', age=27))
    b. Chỉ mục string
        - Nếu muốn lấy các giá trị string ta lấy theo cú pháp sau: str[start:stop:stepover]
        VD: ta có str = "Tôi học Python"
        - Nếu muốn lấy giá trị thứ 5 của chuỗi
            VD: str[5] => "ọ"
        - Nếu muốn lấy giá trị thứ 5 bắt đầu từ phải sang trái
            VD: str[-5] => "y"
        - Nếu muốn lấy giá trị đầu tiên đến giá trị thứ 5
            VD: str[:5] => "Tôi h"
        - Nếu muốn lấy giá trị đầu tiên đến giá trị cuối cùng
            VD: str[:] => "Tôi học Python"
        - Nếu muốn lấy giá trị thứ nhất đến giá trị cuối cùng
            VD: str[1:] => "ôi học Python"
        - Nếu muốn lấy giá trị từ nhất đến giá trị cuối cùng với điều kiện bỏ cách 1 từ xong lấy 1 từ
            VD: str[1::2] => "ô ọ yhn"
        - Nếu muốn lấy giá trị từ đầu đến giá trị cuối cùng và cách 3 từ
            VD: str[::3] => "T cyo"
        - Nếu giá trị = -3
            VD: str[::-3] => "nt hô"

5. Built-In Functions + Methods
    a. Hàm Built-In của Python:
        print(): Hiển thị văn bản hoặc giá trị cụ thể trên màn hình.
        len(): Trả về độ dài của một đối tượng, ví dụ như một chuỗi hoặc một danh sách.
        abs(): Trả về giá trị tuyệt đối của một số.

    b. Phương thức Built-In của Python:
        split(): Chia một chuỗi thành một danh sách các chuỗi con, sử dụng khoảng trắng hoặc một
                ký tự phân tách khác để phân tách.
        join(): Nối các chuỗi con trong một danh sách để tạo ra một chuỗi đơn.
        append(): Thêm một phần tử vào cuối danh sách.
        sort(): Sắp xếp các phần tử của một danh sách theo thứ tự tăng dần hoặc giảm dần.
"""



# Python cơ bản 2
"""
1. List
    - List là một kiểu dữ liệu dùng để lưu trữ các giá trị được phân tách bằng dấu phẩy 
        và đặt trong cặp dấu ngoặc vuông []. Các phần tử trong danh sách có thể là bất kỳ kiểu dữ liệu nào, 
        bao gồm các kiểu dữ liệu phức tạp khác như danh sách lồng nhau hoặc bộ.
        VD: my_list = [1, "apple", True]
    - Chúng ta có thể truy cập các phần tử trong danh sách bằng cách sử dụng chỉ mục (index) của chúng, 
        bắt đầu từ 0. Chúng ta cũng có thể sử dụng chỉ mục âm để truy cập các phần tử từ cuối danh sách.
        VD:
            my_list = [1, 2, 3, 4, 5]
            print(my_list[0]) => 1
            print(my_list[0:3]) => [1,2,3,4]
            print(my_list[-1]) => 5
    - Chúng ta có thể thay đổi giá trị của một phần tử trong danh sách 
        bằng cách truy cập chỉ mục của nó và gán giá trị mới.
        VD:
            my_list = [1, 2, 3, 4, 5]
            my_list[2] = "apple"
            print(my_list)  # kết quả là [1, 2, "apple", 4, 5]
    a. Ma trận

2. Các phương thức làm việc với list
    - list.append(x): Thêm phần tử x vào cuối List.
    - list.insert(i, x): Thêm phần tử x vào vị trí i của List.
    - list.extend(iterable): Thêm các phần tử của iterable vào cuối List.
    - list.remove(x): Xóa phần tử x đầu tiên tìm thấy trong List.
    - list.pop([i]): Xóa phần tử ở vị trí i trong List. Nếu i không được chỉ định, 
        phần tử cuối cùng của List sẽ bị xóa.
    - list.sort(key=None, reverse=False): Sắp xếp các phần tử trong List theo thứ tự tăng dần. 
        key là hàm được sử dụng để tạo ra giá trị so sánh và reverse là một cờ để xác định xem có 
        sắp xếp theo thứ tự giảm dần hay không.
    - list.reverse(): Đảo ngược thứ tự các phần tử trong List.
    - list[index]: Lấy phần tử ở vị trí index trong List.x
    - clear() là một phương thức được sử dụng để xóa tất cả các phần tử trong List
    - index() là một phương thức được sử dụng để tìm kiếm vị trí đầu tiên của một giá trị cụ thể trong List
    - sorted() là một hàm được sử dụng để sắp xếp các phần tử trong một iterable object như List
        VD:
            my_list = [3, 1, 4, 1, 5, 9, 2, 6, 5]
            sorted_list = sorted(my_list, reverse=True)
            print(sorted_list)
            # Output: [9, 6, 5, 5, 4, 3, 2, 1, 1]
        - Phương thức sort() là một phương thức được gọi trên List và sắp xếp các phần tử trong List 
        đó mà không trả về bất kỳ giá trị nào. Trong khi đó, hàm sorted() trả về một List mới chứa 
        các phần tử đã được sắp xếp và không làm thay đổi List ban đầu.
    - join() là một phương thức được sử dụng để ghép các phần tử của một iterable object (như List, 
        Tuple, Set, hoặc String) thành một chuỗi mới, sử dụng một ký tự hoặc chuỗi con nhất định
        để ngăn cách giữa các phần tử
        VD: 
            my_list = ["apple", "banana", "orange"]
            separator = ", "
            result = separator.join(my_list)
            print(result)
            # Output: "apple, banana, orange"
    a. List unpacking
        VD:
            a,b,c, *other, d = [1,2,3,4,5,6,7,8,9]
            print(a) => 1
            print(b) => 2
            print(c) => 3
            print(other) => [4,5,6,7,8]
            print(d) => 9
    b. None = null

3. Dictionary
    - Dictionary là một cấu trúc dữ liệu trong Python cho phép lưu trữ các giá trị có khóa (key) tương ứng.
        Dictionary được biểu diễn bằng một cặp ngoặc nhọn "{}" và chứa các cặp key-value, 
        với mỗi cặp được ngăn cách bởi dấu phẩy.
        VD:
            my_dict = {"name": "John", "age": 30, "city": "New York"}
    a. Dictionary Methods
        - clear(): Xóa tất cả các phần tử khỏi từ điển.
        - copy(): Trả về một bản sao của từ điển.
        - get(key[, default]): Trả về giá trị của khóa được chỉ định. Nếu khóa không tồn tại, 
            phương thức trả về giá trị mặc định. Nếu không có giá trị mặc định được chỉ định, 
            phương thức trả về giá trị None.
        - items(): Trả về một danh sách các cặp khóa-giá trị trong từ điển.
        - keys(): Trả về một danh sách các khóa trong từ điển.
        - pop(key[, default]): Xóa và trả về giá trị của khóa được chỉ định. 
            Nếu khóa không tồn tại và không có giá trị mặc định được chỉ định, 
            phương thức sẽ ném ra một ngoại lệ KeyError.
        - popitem(): Xóa và trả về một cặp khóa-giá trị ngẫu nhiên trong từ điển. 
            Nếu từ điển rỗng, phương thức sẽ ném ra một ngoại lệ KeyError.
        - setdefault(key[, default]): Trả về giá trị của khóa được chỉ định. Nếu khóa không tồn tại, 
            phương thức sẽ thêm khóa mới với giá trị mặc định được chỉ định. 
            Nếu không có giá trị mặc định được chỉ định, phương thức trả về giá trị None.
        - update([other]): Cập nhật từ điển với các cặp khóa-giá trị từ từ điển hoặc 
            iterable object được chỉ định.
        - values(): Trả về một danh sách các giá trị trong từ điển.
        
4. Tuple 
    - Tuple là một kiểu dữ liệu không thay đổi (immutable), giống như list, tuy nhiên, 
        tuple không thể thay đổi sau khi tạo ra.
    - Một tuple được định nghĩa bằng cách sử dụng dấu ngoặc đơn () và 
        các phần tử trong tuple được phân cách bằng dấu phẩy
        VD: 
            t = (1, 2, "Hello", 3.5)
    - Tuple được sử dụng giống như list
    - Một số tính năng của tuple:
        - Không thể thêm, sửa hoặc xóa phần tử từ tuple, vì nó là một kiểu dữ liệu không thay đổi.
        - Vì tuple là không thay đổi, chúng ta có thể sử dụng tuple như là các khóa cho từ điển.
        - Truy xuất phần tử từ tuple nhanh hơn so với list vì tuple được lưu trữ dưới dạng bộ nhớ liên tục, 
            trong khi list thì không phải.

5. Set
    - Set là một kiểu dữ liệu được sử dụng để lưu trữ một tập hợp các phần tử không có thứ tự và không có 
        phần tử trùng lặp. Set được định nghĩa bằng cách sử dụng cặp dấu ngoặc nhọn {} và các 
        phần tử được phân tách bằng dấu phẩy
        VD: 
            s = {1, 2, 3, 4}
    - Các phần tử trong set có thể là bất kỳ kiểu dữ liệu nào, bao gồm cả các kiểu dữ liệu đã được định nghĩa 
        sẵn như int, float, string, tuple, set hoặc thậm chí là các object.
    - Set cũng cung cấp các phép toán hợp, giao, và phần tử của (union, intersection và membership) 
        giống như toán tử trong lý thuyết toán học
        VD: 
            set1 = {1, 2, 3, 4, 5}
            set2 = {3, 4, 5, 6, 7}
            union_set = set1 | set2
            print(union_set)  # In ra {1, 2, 3, 4, 5, 6, 7}
            
            intersection_set = set1 & set2
            print(intersection_set)  # In ra {3, 4, 5}
            
            membership_check = 3 in set1
            print(membership_check)  # In ra True
    a. Các phương thức của set
        - add(element): Thêm một phần tử vào set.
        - clear(): Xóa tất cả các phần tử của set.
        - copy(): Tạo một bản sao của set.
        - difference(set): Trả về một set chứa các phần tử không có trong set được truyền vào.
        - difference_update(set): Xóa các phần tử trong set được truyền vào khỏi set gọi phương thức.
        - discard(element): Xóa phần tử được chỉ định khỏi set nếu nó có trong set.
        - intersection(set): Trả về một set chứa các phần tử chung của set được truyền vào.
        - intersection_update(set): Chỉ giữ các phần tử chung của set được truyền vào và set gọi phương thức.
        - isdisjoint(set): Trả về True nếu hai set không có phần tử chung, ngược lại trả về False.
        - issubset(set): Trả về True nếu set được gọi phương thức là một tập con của set được truyền vào, 
            ngược lại trả về False.
        - issuperset(set): Trả về True nếu set được gọi phương thức là một tập hợp con của set được truyền vào, 
            ngược lại trả về False.
        - pop(): Xóa và trả về một phần tử bất kỳ từ set.
        - remove(element): Xóa phần tử được chỉ định khỏi set nếu nó có trong set. Nếu phần tử không có 
            trong set, sẽ ném ra lỗi KeyError.
        - symmetric_difference(set): Trả về một set chứa các phần tử không chung của cả hai set.
        - symmetric_difference_update(set): Thay đổi set gọi phương thức để chỉ bao gồm các phần tử không 
            chung của cả hai set.
        - union(set): Trả về một set chứa các phần tử từ cả hai set.
        - update(set): Thêm các phần tử từ set được truyền vào vào set gọi phương thức.
"""



# Python cơ bản 3
"""
1. Câu điều kiện
    a. Cú pháp:
        if <condition>:
            # code block 1
        else:
            # code block 2
        - Indentation (thụt đầu dòng) là một phần rất quan trọng trong Python. 
            Indentation được sử dụng để định nghĩa các khối lệnh trong Python, 
            thay vì sử dụng các ký tự như ngoặc nhọn ({}) hoặc từ khóa như "begin" và "end" như trong 
            các ngôn ngữ lập trình khác
    b. Truthy vs Falsey
        - Trong Python, các giá trị có thể được đánh giá như là True hoặc False trong các 
            tình huống khác nhau. Các giá trị được đánh giá là True được gọi là "truthy", 
            còn các giá trị được đánh giá là False được gọi là "falsey".
        - Các giá trị falsey trong Python bao gồm:
            + False
            + None
            + Số 0 (int hoặc float)
            + Chuỗi rỗng ("")
            + Danh sách rỗng ([])
            + Tập hợp rỗng (set())
            + Từ điển rỗng ({})
            + Giá trị False của các đối tượng có thể được định nghĩa bởi người dùng (nếu có)
            
        - Các giá trị truthy trong Python bao gồm:
            + True
            + Bất kỳ số khác không (ngoại trừ số phức)
            + Chuỗi không rỗng (có một hoặc nhiều ký tự)
            + Danh sách không rỗng (có ít nhất một phần tử)
            + Tập hợp không rỗng (có ít nhất một phần tử)
            + Từ điển không rỗng (có ít nhất một cặp key-value)
            + Bất kỳ đối tượng nào được định nghĩa bởi người dùng có giá trị khác None (nếu có)
    c. Ternary Operator
        - Ternary operator cho phép ta viết một biểu thức có điều kiện trực tiếp trong 
            một dòng code, thay vì phải viết một khối lệnh if-else hoặc một hàm.
            VD: <expression1> if <condition> else <expression2>
                Trong đó:
                    <condition> là điều kiện được kiểm tra, 
                    <expression1> là giá trị được trả về nếu <condition> là True, 
                    <expression2> là giá trị được trả về nếu <condition> là False.
    d. Short Circuiting
        - && được thay thế bằng 'and'
        - || được thay thế bằng 'or'
        - Phủ định thì được gọi bằng câu lệnh 'not'
        - Để xem 2 giá trị có cùng địa chỉ bộ nhớ hay không ta dùng câu lệnh 'is'
        - Ngoài ra còn có các toán tử logic: 
            >, <: Nhỏ hơn, lớn hơn
            ==: Bằng
            <=, >=: Nhỏ hơn hoặc bằng, lớn hơn hoặc bằng
            !=: Khác

2. Vòng lặp
    a. For
        - Vòng lặp for trong Python được sử dụng để lặp qua một tập hợp các giá trị 
            như danh sách, bộ, chuỗi hoặc các đối tượng có thể lặp lại
            VD: 
                for variable in iterable:
                    # code to execute
        - range(): range() là một hàm được sử dụng để tạo ra một chuỗi số nguyên liên tiếp trong một khoảng 
            giá trị. Cú pháp của hàm range là: range(start, stop, step)
            Với: 
                start (không bắt buộc): giá trị đầu tiên trong chuỗi. Nếu không được chỉ định, mặc định là 0.
                stop (bắt buộc): giá trị cuối cùng trong chuỗi. Chuỗi sẽ không bao gồm giá trị này. 
                    Ví dụ, range(0, 3) sẽ tạo ra chuỗi 0, 1, 2.
                step (không bắt buộc): khoảng cách giữa các giá trị trong chuỗi. 
                    Nếu không được chỉ định, mặc định là 1.
        - enumerate() là một hàm built-in của Python, được sử dụng để lặp qua một chuỗi (list, tuple, string, ...) 
            và đồng thời trả về cả vị trí chỉ số (index) và giá trị tương ứng của từng phần tử trong chuỗi. 
            Cú pháp của hàm enumerate() là: enumerate(iterable, start=0)
                VD:
                    fruits = ['apple', 'banana', 'orange']
                    for index, fruit in enumerate(fruits):
                        print(index, fruit)    
                    
                    Output: 
                        0 apple
                        1 banana
                        2 orange
    b. While
        - while là một câu lệnh điều khiển vòng lặp. Câu lệnh while được sử dụng để 
            lặp lại một khối lệnh cho đến khi điều kiện kiểm tra trở thành False.
            Cú pháp của câu lệnh while là: 
                while condition:
                    # code block
                Trong đó:
                    condition: là điều kiện kiểm tra được đánh giá trước mỗi lần lặp lại khối lệnh. 
                        Nếu điều kiện kiểm tra là True, khối lệnh được thực hiện. 
                        Nếu điều kiện kiểm tra là False, vòng lặp kết thúc và chương trình 
                        tiếp tục thực hiện các câu lệnh sau khối lệnh while.
                    code block: là khối lệnh được thực hiện khi điều kiện kiểm tra là True.
                    VD:
                        i = 0
                        while i < 5:
                            print(i)
                            i += 1
                    Output: 0, 1, 2, 3, 4, 5
        
        -  break, continue, pass
            - break: là câu lệnh dùng để kết thúc vòng lặp. Khi câu lệnh break được gọi, 
                chương trình sẽ dừng vòng lặp và tiếp tục thực hiện các câu lệnh sau vòng lặp.
            
            - continue: là câu lệnh dùng để bỏ qua lần lặp hiện tại và tiếp tục với lần lặp tiếp theo. 
                Khi câu lệnh continue được gọi, các câu lệnh trong khối lệnh sau nó sẽ bị bỏ qua và 
                chương trình sẽ tiếp tục thực hiện vòng lặp.
                
            - pass: là câu lệnh không làm gì cả, chỉ đóng vai trò giữ chỗ. Khi câu lệnh pass được gọi, 
                chương trình sẽ bỏ qua câu lệnh đó và tiếp tục thực hiện các câu lệnh khác.
"""



# Python cơ bản 4
"""
1. Hàm
    -  Hàm (function) là một khối mã độc lập có chức năng thực hiện một nhiệm vụ cụ thể. 
        Hàm có thể được sử dụng nhiều lần trong chương trình để thực hiện các tác vụ tương tự mà 
        không cần phải viết lại mã nhiều lần.
        VD:
            def greet():
                print("Hello")
                
            def greet()
    a. Parameters and Arguments (Tham số và đối số)
        - Parameters (tham số) là một biến được định nghĩa trong định nghĩa của hàm hoặc phương thức. 
            Parameter đại diện cho giá trị đầu vào mà hàm cần để thực hiện một tác vụ nào đó. 
            Mỗi hàm hoặc phương thức có thể có một hoặc nhiều tham số.
            VD: 
                def add(x, y):
                    return x + y  
        - Argument (đối số) là giá trị thực sự được truyền cho tham số của hàm hoặc phương thức khi ta gọi nó. 
            Argument đại diện cho giá trị cụ thể được sử dụng bên trong hàm hoặc phương thức 
            để thực hiện một tác vụ cụ thể.
            VD: result = add(3, 5)
    b. Default Parameters and Keyword Arguments
        - Default parameters là giá trị mặc định được gán cho một tham số trong hàm. Khi gọi hàm, 
            nếu không truyền giá trị cho tham số này, thì giá trị mặc định sẽ được sử dụng.     
            VD:
                def print_greeting(name="World"):
                    print(f"Hello, {name}!")
                
                print_greeting()  # output: Hello, World!
                print_greeting("John")  # output: Hello, John!
        - Keyword arguments là cách truyền giá trị cho tham số trong hàm bằng cách chỉ định tên của tham số đó.
            VD:
                def print_info(name, age):
                    print(f"Name: {name}, Age: {age}")
                
                print_info(name="John", age=30)
    c. Return
        - return là một câu lệnh dùng để trả về giá trị từ một hàm. Khi một hàm được gọi và thực thi, 
            nếu có câu lệnh return được gọi, giá trị trả về sẽ được truyền lại cho phần gọi hàm.   
            VD: 
                def add_numbers(x, y):
                    sum = x + y
                    return sum
                
                result = add_numbers(2, 3)
                print(result)  # output: 5
        - Nếu một hàm không có câu lệnh return, thì giá trị trả về của hàm đó sẽ là None
    d. Methods vs Functions
        - Trên một mức độ cơ bản, method và function đều là các khối lệnh trong chương trình 
            để thực hiện các tác vụ nhất định. Tuy nhiên, chúng có một số sự khác biệt quan trọng.
        - Một function là một khối lệnh độc lập trong chương trình, thường nhận vào đầu vào 
            (có thể có hoặc không) và trả về đầu ra (có thể có hoặc không). 
            Function thực hiện một số tác vụ và trả về kết quả sau khi hoàn thành các tác vụ đó. 
            Function có thể được gọi ở nhiều nơi khác nhau trong chương trình.
            VD: 
                def calculate_sum(numbers_list):
                    sum = 0
                    for number in numbers_list:
                        sum += number
                    return sum
        - Một method là một function liên kết với một đối tượng hoặc một lớp. 
            Method có thể truy cập và thao tác trực tiếp với các thuộc tính của đối tượng 
            hoặc các phương thức khác của lớp. 
            Method thường được gọi bằng cách sử dụng cú pháp "object.method()", 
            trong đó object là một đối tượng của lớp đó.
            VD: 
                class Person:
                    def __init__(self, name, age):
                        self.name = name
                        self.age = age
                
                    def get_info(self):
                        return f"Name: {self.name}, Age: {self.age}"
                
                person = Person("John", 30)
                info = person.get_info()
                print(info)  # output: Name: John, Age: 30
    e. *args and **kwargs
        - *args là một tuple chứa các tham số được truyền vào hàm dưới dạng danh sách các đối số, 
            nghĩa là số lượng tham số có thể thay đổi. Đây là cách tiếp cận thường được sử dụng khi 
            chúng ta muốn truyền một số lượng tham số không xác định vào hàm.
                VD:
                    def my_function(*args):
                        for arg in args:
                            print(arg)
                        
                    my_function('Hello', 'world', '!')
                Output:
                    Hello
                    world
                    !
        - **kwargs là một dictionary chứa các tham số được truyền vào hàm dưới dạng các cặp key-value, 
            nghĩa là số lượng tham số có thể thay đổi và được đặt tên. 
            Đây là cách tiếp cận thường được sử dụng khi chúng ta muốn truyền một số lượng tham số 
            không xác định vào hàm và chúng ta muốn đặt tên cho từng tham số.
                VD:
                    def my_function(**kwargs):
                        for key, value in kwargs.items():
                            print(f'{key} = {value}')
                        
                    my_function(name='John', age=25, gender='male')
                Output: 
                    name = John
                    age = 25
                    gender = male
    f. Cú pháp của Walrus Operator
        - Cú pháp := được sử dụng trong các biểu thức điều kiện, trong đó giá trị được gán vào biến là 
            kết quả của biểu thức đó.
            VD:
                while (s := input("Nhập chuỗi: ")) != "stop":
                    print(f"Độ dài chuỗi là {len(s)}")
            - Trong ví dụ trên, biểu thức điều kiện (s := input("Nhập chuỗi: ")) != "stop" sẽ trả về 
                giá trị của biến s và kiểm tra nó có khác "stop" hay không. Nếu biến s khác "stop", 
                thì sẽ in ra độ dài của chuỗi đó.
2. Scope
    - Scope trong Python là một khối mã trong đó các biến có thể được truy cập và sử dụng. 
        Python có hai loại phạm vi (scope): Global scope và Local scope.
    - Global scope là phạm vi toàn cục, nghĩa là các biến được định nghĩa ở đây có thể được truy cập và 
        sử dụng ở bất kỳ nơi nào trong chương trình Python của bạn. Để định nghĩa một biến trong global scope, 
        bạn có thể khai báo nó bên ngoài mọi hàm hoặc lớp trong chương trình của bạn.
        VD:
            x = 10
            def print_x():
                print(x)
            print_x() # Output: 10
    - Local scope là phạm vi cục bộ, nghĩa là các biến được định nghĩa ở đây chỉ có thể được truy cập và 
        sử dụng trong phạm vi của hàm hoặc lớp mà chúng được định nghĩa.
        VD:
            def print_x():
                x = 10
                print(x)
            print_x() # Output: 10
    - Nếu bạn cố gắng truy cập một biến ở trong local scope của một hàm hoặc lớp từ bên ngoài phạm vi 
        của nó, bạn sẽ nhận được một lỗi "NameError".
        VD:
            def print_x():
                x = 10
            print(x) # NameError: name 'x' is not defined
    - Khi có một biến được định nghĩa cả trong global scope và local scope, biến ở local scope sẽ 
        được ưu tiên sử dụng.
        VD:
            x = 10
            def print_x():
                x = 20
                print(x)
            print_x() # Output: 20
"""



# Python cơ bản 5
"""
1. Cài đặt môi trường python

"""



# Python cơ bản 6
"""
1. OOP
    - 
2. Attributes and Methods
    - Thuộc tính (Attributes) trong Python là các biến thuộc về đối tượng đó. 
        Chúng ta có thể truy cập thuộc tính của một đối tượng bằng cách sử dụng toán tử dấu chấm (dot) "."
    - Phương thức (Methods) trong Python là các hàm thuộc về đối tượng đó. Chúng ta có thể gọi một 
        phương thức của một đối tượng bằng cách sử dụng cú pháp sau:
        VD: object.method_name(arguments)
3. __init__
    - Trong Python, phương thức __init__() là một phương thức đặc biệt trong một lớp (class). 
        Phương thức này được gọi khi một đối tượng (object) được tạo ra từ lớp đó.
    - Cú pháp:
        class ClassName:
            def __init__(self, parameter1, parameter2, ...):
                self.attribute1 = parameter1
                self.attribute2 = parameter2
                ...
    - Trong đó, tham số đầu tiên của phương thức __init__() là self, đại diện cho chính đối tượng được tạo ra. 
        Các tham số khác được sử dụng để khởi tạo các thuộc tính (attributes) của đối tượng.
        VD:
            class Rectangle:
                def __init__(self, length, width):
                    self.length = length
                    self.width = width
            - Khi bạn tạo một đối tượng từ lớp Rectangle, phương thức __init__() sẽ được gọi tự động, 
                và các thuộc tính length và width của đối tượng sẽ được khởi tạo với các giá trị được truyền vào
                rect = Rectangle(10, 5) #Tạo một đối tượng Rectangle với chiều dài 10 và chiều rộng 5
                print(rect.length) #In ra 10
                print(rect.width) #In ra 5
    - Phương thức __init__() được sử dụng để khởi tạo các thuộc tính của đối tượng, và nó cũng có thể 
        được sử dụng để thực hiện các thao tác khác cần thiết để chuẩn bị cho việc sử dụng đối tượng đó
3. @classmethod and @staticmethod
    - Cả hai đều là các phương thức mà không cần tạo ra một đối tượng mới từ lớp để gọi chúng.
    - Phương thức @classmethod là một phương thức được gắn với lớp đó chứ không phải với một đối tượng 
        cụ thể nào của lớp đó. Nó thường được sử dụng khi cần truy cập các biến lớp (class variables) 
        hoặc phương thức lớp (class methods). Để đánh dấu một phương thức là @classmethod, 
        ta sử dụng decorator @classmethod trước phương thức đó.
        VD:
            - Ví dụ, trong lớp đại diện cho một hình chữ nhật, ta muốn định nghĩa một phương thức để 
                tính diện tích của hình chữ nhật dựa trên chiều dài và chiều rộng của nó. 
                Để làm điều đó, ta cần sử dụng biến lớp PI và phương thức lớp circle_area():
                    class Rectangle:
                        PI = 3.14
    
                        def __init__(self, length, width):
                            self.length = length
                            self.width = width
                        
                        @classmethod
                        def from_square(cls, side_length):
                            return cls(side_length, side_length)
                        
                        @classmethod
                        def circle_area(cls, radius):
                            return cls.PI * radius ** 2
                        
                        def area(self):
                            return self.length * self.width
        - cls là một tham số đặc biệt thường được sử dụng trong các phương thức của các lớp (classes). 
            cls thường được sử dụng để tham chiếu đến lớp đang được xử lý trong các phương thức của nó
    - Phương thức @staticmethod là một phương thức tĩnh không gắn liền với lớp hoặc đối tượng. 
        Nó giống như một hàm thông thường bên ngoài lớp. Để đánh dấu một phương thức là @staticmethod, 
        ta sử dụng decorator @staticmethod trước phương thức đó.                
        VD:
            - Ví dụ, ta muốn định nghĩa một phương thức để kiểm tra xem một chuỗi có phải là một số nguyên 
                hay không. Ta có thể định nghĩa một phương thức @staticmethod như sau:
                class Utility:
                    @staticmethod
                    def is_integer(s):
                        try:
                            int(s)
                            return True
                        except ValueError:
                            return False
    - Để gọi phương thức @classmethod và @staticmethod, ta không cần tạo ra một đối tượng mới từ lớp, 
        mà có thể gọi chúng trực tiếp từ lớp:
        VD:
            # Sử dụng phương thức @classmethod
            rect = Rectangle.from_square(5)
            print(rect.length, rect.width) # In ra 5 5
            print(Rectangle.circle_area(2)) # In ra 12.56
            
            # Sử dụng phương thức @staticmethod
            print(Utility.is_integer("123")) # In ra True
            print(Utility.is_integer("abc")) # In ra False
"""



# Python cơ bản 7
"""
1. Tính đóng gói
    a. Định nghĩa
        - Encapsulation là một trong những nguyên tắc cơ bản trong lập trình hướng đối tượng, 
            nó cho phép che giấu thông tin và các chi tiết triển khai của đối tượng khỏi các đối tượng khác.
        - Encapsulation thường được thực hiện bằng cách sử dụng các thuộc tính (attributes) và 
            phương thức (methods) của lớp.
        - Các thuộc tính và phương thức của một lớp có thể được khai báo với mức độ truy cập bằng cách sử dụng các 
            từ khóa đặc biệt như public, private và protected.
            - public: thuộc tính và phương thức có mức độ truy cập public có thể được truy cập từ bất kỳ đâu 
                trong chương trình.
            - private: thuộc tính và phương thức có mức độ truy cập private chỉ có thể được truy cập trong 
                phạm vi của lớp chứa chúng. Trong Python, mức độ truy cập private được định nghĩa bằng cách 
                đặt một dấu gạch chân dưới trước tên thuộc tính hoặc phương thức.
            - protected: thuộc tính và phương thức có mức độ truy cập protected chỉ có thể được truy cập 
                từ bên trong lớp chứa chúng hoặc từ bên trong các lớp con của lớp chứa chúng. 
                Trong Python, mức độ truy cập protected được định nghĩa bằng cách đặt một dấu gạch chân dưới 
                trước tên thuộc tính hoặc phương thức, và đặt một dấu gạch chân dưới trước dấu gạch chân dưới 
                đầu tiên.
            VD: 
                class MyClass:
                    def __init__(self, public_attribute, _protected_attribute, __private_attribute):
                        self.public_attribute = public_attribute
                        self._protected_attribute = _protected_attribute
                        self.__private_attribute = __private_attribute
                
                    def public_method(self):
                        print("This is a public method")
                
                    def _protected_method(self):
                        print("This is a protected method")
                
                    def __private_method(self):
                        print("This is a private method")
                
                my_object = MyClass("public", "protected", "private")
                print(my_object.public_attribute)    # Output: public
                print(my_object._protected_attribute)    # Output: protected
                print(my_object.__private_attribute)    # Output: AttributeError: 'MyClass' object has no attribute '__private_attribute'
                my_object.public_method()    # Output: This is a public method
                my_object._protected_method()    # Output: This is a protected method
                my_object.__private_method()    # Output: AttributeError: 'MyClass' object has no attribute '__private_method'

2. Tính trừu tượng
    - Abstraction là một trong những nguyên tắc cơ bản trong lập trình hướng đối tượng, nó cho phép che 
        giấu chi tiết triển khai của một đối tượng và chỉ hiển thị các thông tin cần thiết để sử dụng 
        đối tượng đó. Trong Python, Abstraction thường được thực hiện bằng cách sử dụng các lớp 
        trừu tượng (abstract classes) và phương thức trừu tượng (abstract methods).
    - Lớp trừu tượng là một lớp mà không thể tạo ra các đối tượng trực tiếp, mà chỉ được sử dụng như một 
        bộ khung (template) để định nghĩa các lớp con. Lớp trừu tượng thường chứa các phương thức trừu tượng, 
        các phương thức này chỉ có định nghĩa mà không có triển khai cụ thể. Các lớp con của lớp trừu tượng 
        phải triển khai các phương thức trừu tượng này.
    - Phương thức trừu tượng là một phương thức mà không có triển khai cụ thể, chỉ có định nghĩa. 
        Phương thức trừu tượng chỉ được định nghĩa trong các lớp trừu tượng, và các lớp con phải 
        triển khai các phương thức trừu tượng này.
        VD:
            from abc import ABC, abstractmethod

            class Animal(ABC):
                @abstractmethod
                def move(self):
                    pass
                
            class Dog(Animal):
                def move(self):
                    print("Dog walks and runs")
                
            class Bird(Animal):
                def move(self):
                    print("Bird flies")
                
            # animal = Animal()    # Output: TypeError: Can't instantiate abstract class Animal with abstract methods move
                
            dog = Dog()
            dog.move()    # Output: Dog walks and runs
                
            bird = Bird()
            bird.move()    # Output: Bird flies
                
        - Trong ví dụ trên, Animal là một lớp trừu tượng, và move() là một phương thức trừu tượng. 
            Lớp Dog và Bird là các lớp con của Animal, và chúng phải triển khai phương thức move(). 
            Khi chúng ta cố gắng tạo ra một đối tượng của lớp trừu tượng Animal, 
            Python sẽ gây ra lỗi TypeError vì không thể tạo ra một đối tượng trực tiếp từ một lớp trừu tượng.
    a. Private và Public
        - Trong Python, các biến (variable) có thể được khai báo là private hoặc public. 
            Các biến public có thể được truy cập từ bên ngoài lớp, trong khi các biến private chỉ 
            có thể được truy cập trong lớp. Đây là cách thức triển khai Encapsulation trong Python.
        - Các biến private được định nghĩa bằng cách bắt đầu bằng dấu gạch chân đôi (__), 
            trong khi các biến public không có dấu gạch chân đôi. Tuy nhiên, trong Python, 
            các biến private thực sự vẫn có thể truy cập từ bên ngoài lớp, bằng cách sử dụng tên 
            của biến với một tiền tố _TênLớp__tênBiến.
            VD:
                class Person:
                    def __init__(self, name, age):
                        self.name = name  # Public variable
                        self.__age = age  # Private variable
                
                    def display(self):
                        print("Name:", self.name)
                        print("Age:", self.__age)
                
                person = Person("Alice", 25)
                
                person.display()
                # Output:
                # Name: Alice
                # Age: 25
                
                print(person.name)     # Output: Alice
                print(person.__age)    # Output: AttributeError: 'Person' object has no attribute '__age'
                print(person._Person__age)   # Output: 25
                
            - Trong ví dụ này, biến name là một biến public và có thể truy cập từ bên ngoài lớp Person. 
                Biến __age là một biến private và chỉ có thể truy cập trong lớp Person. 
                Tuy nhiên, chúng ta có thể truy cập biến __age từ bên ngoài lớp bằng cách sử dụng _Person__age.
        - Việc sử dụng tiền tố _ để chỉ ra biến protected không phải là một quy tắc trong Python, 
            đó chỉ là một quy ước chung được sử dụng trong một số ngôn ngữ lập trình hướng đối tượng.
    
3. Tính kế thừa
    - Inheritance (Kế thừa) là cho phép một lớp có thể kế thừa tất cả các thuộc tính và phương thức 
        của lớp khác. Lớp con có thể mở rộng hoặc ghi đè các thuộc tính và phương thức của lớp cha, 
        hoặc có thể thêm các thuộc tính và phương thức mới.
    - Để kế thừa một lớp trong Python, ta chỉ cần đưa tên của lớp cha vào trong dấu ngoặc đơn của lớp con.
        VD:
            class Animal:
                def __init__(self, name):
                    self.name = name
            
                def speak(self):
                    print("Animal speaks")
            
            class Dog(Animal):
                def __init__(self, name):
                    super().__init__(name)
            
                def speak(self):
                    print("Dog barks")
            
            dog = Dog("Buddy")
            print(dog.name)   # Output: Buddy
            dog.speak()       # Output: Dog barks
            
    - Chúng ta có thể sử dụng hàm super() để gọi phương thức của lớp cha từ trong lớp con. 
        Hàm super() trả về một đối tượng của lớp cha và cho phép chúng ta gọi phương thức của lớp cha 
        mà không cần đưa tên của lớp cha vào.
        
    - Chúng ta có thể sử dụng hàm isinstance() để kiểm tra một đối tượng có thuộc về một lớp nào đó hay không.
        VD:
            animal = Animal("Bob")
            dog = Dog("Buddy")
            
            print(isinstance(animal, Animal))   # Output: True
            print(isinstance(dog, Animal))      # Output: True
            print(isinstance(animal, Dog))      # Output: False
        - Trong ví dụ này, animal là một đối tượng thuộc lớp Animal, dog là một đối tượng thuộc lớp Dog. 
            isinstance() trả về True nếu đối tượng thuộc lớp đó hoặc là một lớp con của lớp đó, và False nếu không.

4. Tính đa hình
    - Polymorphism là khả năng của đối tượng để có thể hiển thị hành vi khác nhau tùy theo ngữ cảnh sử dụng. 
        Trong Python, polymorphism được đạt được thông qua việc sử dụng đa hình đa hình (polymorphic) 
        và hàm đa hình (polymorphic functions).
    - Đa hình đa hình (polymorphic) là khả năng của các đối tượng có thể được sử dụng trong 
        nhiều ngữ cảnh khác nhau. Ví dụ, trong Python, một danh sách (list) có thể chứa bất kỳ 
        kiểu đối tượng nào, bao gồm cả số, chuỗi, đối tượng, hàm, v.v. Điều này có nghĩa là chúng ta có thể 
        sử dụng các phương thức chung của danh sách như append(), insert(), remove() cho tất cả các kiểu 
        đối tượng trong danh sách mà không cần phải quan tâm đến kiểu của đối tượng đó.
    - Hàm đa hình (polymorphic functions) là hàm có thể chấp nhận đối số với các kiểu dữ liệu khác nhau 
        và trả về các giá trị khác nhau tùy thuộc vào kiểu dữ liệu của đối số đó. 
        Ví dụ, trong Python, hàm len() có thể được sử dụng để đếm số phần tử trong danh sách, 
        chuỗi hoặc bất kỳ đối tượng nào có thể được đếm được.
        VD:
            class Animal:
                def __init__(self, name):
                    self.name = name
            
                def speak(self):
                    raise NotImplementedError("Subclass must implement abstract method")
            
            class Cat(Animal):
                def speak(self):
                    return "Meow"
            
            class Dog(Animal):
                def speak(self):
                    return "Woof"
            
            def animal_speak(animal):
                print(animal.speak())
            
            cat = Cat("Whiskers")
            dog = Dog("Fido")
            
            animal_speak(cat) # prints "Meow"
            animal_speak(dog) # prints "Woof"
"""



# Python cơ bản 8
"""
1. Object Introspection
    - Object introspection là khả năng của Python để xem xét các đối tượng trong chương trình và truy xuất 
        các thông tin về chúng trong thời gian chạy (runtime)
    - Object introspection cho phép bạn khám phá các đối tượng và xem xét các thuộc tính, phương thức, kiểu, 
        các thông tin của đối tượng và các thành phần khác của đối tượng.
    - Các hàm và phương thức tích hợp để thực hiện object introspection:
        - type(): Hàm này trả về kiểu của một đối tượng
            VD:
                x = 5
                print(type(x))  # Output: <class 'int'>
        - dir(): Hàm này trả về danh sách các thuộc tính và phương thức của một đối tượng.
        - hasattr(): Hàm này trả về giá trị True nếu đối tượng có thuộc tính được chỉ định và False 
            nếu không có.
        - getattr(): Hàm này trả về giá trị của thuộc tính được chỉ định của một đối tượng.
        
2. Dunder Methods
    - Dunder methods (còn được gọi là special methods hoặc magic methods) 
        là các phương thức đặc biệt trong Python có tên bắt đầu và kết thúc bằng hai dấu gạch dưới (underscore), 
        ví dụ như __init__, __str__, __eq__, __lt__, __len__, và nhiều hơn nữa.
    - Các phương thức này được sử dụng để định nghĩa các hành vi đặc biệt cho các lớp, đối tượng và 
        các toán tử trong Python. Khi định nghĩa một lớp và sử dụng một trong các phương thức dunder, 
        ta có thể tùy chỉnh cách lớp được sử dụng trong các toán tử, các phép so sánh, các phép toán số học, 
        cách lớp được chuyển đổi thành chuỗi và nhiều hơn nữa.
        VD: 
            + phương thức __str__ được sử dụng để chuyển đổi đối tượng thành một chuỗi
            + phương thức __eq__ được sử dụng để so sánh hai đối tượng có bằng nhau hay không
            + phương thức __len__ được sử dụng để trả về độ dài của một đối tượng
        VD: 
            class Person:
                def __init__(self, name, age):
                    self.name = name
                    self.age = age
            
                def __str__(self):
                    return f"{self.name} is {self.age} years old."
            
                def __eq__(self, other):
                    return self.name == other.name and self.age == other.age
            
            person1 = Person("Alice", 25)
            person2 = Person("Bob", 30)
            
            print(person1)  # Output: "Alice is 25 years old."
            print(person1 == person2)  # Output: False
    
3. Đa kế thừa
    - Multiple inheritance trong Python là khả năng cho một lớp kế thừa các thuộc tính và phương thức 
        từ nhiều lớp cha khác nhau.
    - Để sử dụng multiple inheritance trong Python, chúng ta chỉ cần liệt kê các lớp cha mà lớp con 
        muốn kế thừa, cách nhau bởi dấu phẩy, trong dấu ngoặc đơn khi khai báo lớp con.
        VD:
            class A:
                def method(self):
                    print("A")
            
            class B:
                def method(self):
                    print("B")
            
            class C(A, B):
                pass
            
            c = C()
            c.method()  # Output: A
        - Trong ví dụ trên, chúng ta đã định nghĩa hai lớp cha A và B, mỗi lớp cha đều có một phương thức 
            có cùng tên là method. Chúng ta đã định nghĩa lớp C kế thừa từ hai lớp cha A và B bằng cách 
            liệt kê chúng trong dấu ngoặc đơn khi khai báo lớp C.
        - Khi chúng ta gọi phương thức method trên đối tượng của lớp C, Python sẽ tìm kiếm phương thức này 
            trong lớp C trước. Nếu không tìm thấy, nó sẽ tìm kiếm trong các lớp cha theo thứ tự được 
            khai báo trong khai báo lớp con (trong trường hợp này là A trước, sau đó là B). 
            Do đó, khi gọi phương thức method trên đối tượng của lớp C, nó sẽ gọi phương thức 
            method được định nghĩa trong lớp A.
        - Tuy nhiên, multiple inheritance cũng có thể dẫn đến một số vấn đề như trùng tên phương thức 
            hoặc thuộc tính trong các lớp cha khác nhau. Khi đó, ta cần quyết định rõ ràng phương thức 
            hay thuộc tính nào sẽ được ưu tiên sử dụng bằng cách sử dụng các quy tắc đặc biệt của Python, 
            chẳng hạn như super() để gọi phương thức của lớp cha tiếp theo trong thứ tự kế thừa.

4. Method Resolution Order
    - MRO trong Python là quá trình tìm kiếm và xác định thứ tự các phương thức được kế thừa 
        trong trường hợp multiple inheritance, tức là khi một lớp con kế thừa từ nhiều lớp cha.
    - MRO giúp Python xác định thứ tự kế thừa phù hợp với nguyên tắc "càng gần thì ưu tiên". 
        MRO được áp dụng bởi các phương thức super() để gọi đến phương thức của lớp cha trực tiếp 
        tiếp theo trong thứ tự kế thừa.
    - Trong Python, MRO được xác định bằng cách sử dụng giải thuật C3. Khi một lớp con được khởi tạo, 
        Python sẽ tạo ra một thứ tự kế thừa tạm thời dựa trên các lớp cha được khai báo, và sau đó 
        áp dụng giải thuật C3 để xác định thứ tự kế thừa chính thức.
        VD:
            class A:
                def method(self):
                    print("A")
            
            class B(A):
                pass
            
            class C(A):
                def method(self):
                    print("C")
            
            class D(B, C):
                pass
            
            d = D()
            d.method()  # Output: C
            
        - Trong ví dụ này, lớp D kế thừa từ lớp B và lớp C, hai lớp cha này lại kế thừa từ lớp A. 
            MRO của lớp D sẽ được xác định như sau: D -> B -> C -> A -> object.
        - Khi gọi phương thức method trên đối tượng của lớp D, Python sẽ tìm kiếm phương thức này theo 
            thứ tự được xác định bởi MRO. Do lớp C định nghĩa phương thức method, phương thức này sẽ 
            được gọi trên đối tượng của lớp D, và kết quả đầu ra sẽ là "C".
    - MRO là một cơ chế quan trọng để giải quyết các vấn đề liên quan đến multiple inheritance trong Python, 
        và nó được tự động áp dụng bởi Python trong quá trình tìm kiếm phương thức được kế thừa.
"""



# Python cơ bản 9
"""
1. Pure Functions
    - Pure Functions được định nghĩa như những hàm không thay đổi bất kỳ trạng thái nào bên ngoài hàm và trả về 
        kết quả duy nhất dựa trên đầu vào của nó.
    - Để định nghĩa một hàm Pure trong Python, chúng ta cần đảm bảo rằng hàm không sử dụng hoặc thay đổi bất kỳ 
        biến nào ngoài hàm và không có bất kỳ tác động nào đến các đối tượng khác trong chương trình.
        VD:
            def add_numbers(x, y):
                return x + y
        - Hàm add_numbers() là một hàm Pure vì nó không thay đổi bất kỳ biến hoặc trạng thái nào bên ngoài hàm và 
            chỉ trả về kết quả của phép tính toán dựa trên đầu vào của nó.
    - Tuy nhiên, nếu hàm sử dụng hoặc thay đổi biến hoặc trạng thái bên ngoài, ví dụ như in ra một thông báo hoặc 
        thay đổi giá trị của một biến toàn cục, thì hàm đó sẽ không được xem là hàm Pure.

2. map()
    - map() là một hàm được sử dụng để áp dụng một hàm (function) lên mỗi phần tử của một danh sách (iterable) 
        và trả về một iterator chứa các giá trị đã được thay đổi bởi hàm đó.
    - Cú pháp: map(function, iterable)
        Trong đó:
            + function: Là hàm mà bạn muốn áp dụng lên các phần tử trong iterable.
            + iterable: Là một danh sách, tuple hoặc bất kỳ đối tượng nào có thể lặp lại.
        VD:
            numbers = [1, 2, 3, 4, 5]
            result = map(lambda x: x * 2, numbers)
            
            print(list(result))
            
            output: [2, 4, 6, 8, 10]
    - Trong ví dụ này, ta sử dụng hàm lambda để định nghĩa hàm nhân mỗi phần tử trong danh sách với 2, 
        và truyền nó vào hàm map() cùng với danh sách numbers. Kết quả trả về của hàm map() được chuyển đổi 
        thành một danh sách bằng cách sử dụng hàm list().
    
3. filter()
    - filter() là một hàm được sử dụng để lọc các phần tử của một danh sách (iterable) dựa trên một 
        điều kiện cho trước và trả về một iterator chứa các phần tử đã được lọc.
    - Cú pháp: filter(function, iterable)
        Trong đó:
            function: Là hàm định nghĩa điều kiện lọc các phần tử của danh sách. Hàm này sẽ được 
                áp dụng lên từng phần tử của danh sách và trả về giá trị True hoặc False.
            iterable: Là một danh sách, tuple hoặc bất kỳ đối tượng nào có thể lặp lại.
        VD:
            numbers = [1, 2, 3, 4, 5]
            result = filter(lambda x: x % 2 == 0, numbers)
            
            print(list(result))
            
            => Đầu ra sẽ là [2, 4]
        - hàm lambda sẽ được tìm hiểu ở các phần sau

4. zip()
    - zip() là một hàm được sử dụng để kết hợp các phần tử của các danh sách (iterables) khác nhau 
        và trả về một iterator chứa các cặp phần tử tương ứng.
    - Cú pháp: zip(*iterables)
        Trong đó: iterables: Là các danh sách, tuple hoặc bất kỳ đối tượng nào có thể lặp lại.
        VD:
            a = [1, 2, 3]
            b = ['a', 'b', 'c']
            result = zip(a, b)
            
            print(list(result))
            => Đầu ra sẽ là [(1, 'a'), (2, 'b'), (3, 'c')].
            - Để chuyển đổi iterator này thành một danh sách, ta sử dụng hàm list().
    
5. reduce()
    - reduce() là một hàm được sử dụng để áp dụng một hàm cho từng cặp phần tử của một danh sách (iterable), 
        kết hợp chúng thành một giá trị duy nhất và trả về giá trị đó.
    - Để sử dụng hàm reduce() trong Python, trước tiên bạn cần import module functools.
    - Cú pháp: reduce(function, iterable, initializer=None)
        Trong đó: 
            function: Là hàm được sử dụng để kết hợp từng cặp phần tử của danh sách. 
                Hàm này nhận hai tham số và trả về một giá trị.
            iterable: Là một danh sách, tuple hoặc bất kỳ đối tượng nào có thể lặp lại.
            initializer: Là một giá trị tùy chọn được sử dụng làm giá trị khởi đầu cho quá trình reduce.
        VD: 
            from functools import reduce

            numbers = [1, 2, 3, 4, 5]
            result = reduce(lambda x, y: x + y, numbers)
            
            print(result)
            
            => Đầu ra sẽ là 15.
    
6. Lambda Expressions
    - Lambda Expression trong Python là một cách tạo ra hàm vô danh (anonymous function) mà không 
        cần phải đặt tên hàm. Đây là một phần của tính năng hàm bậc cao (higher-order functions) 
        trong Python, nó cho phép chúng ta tạo ra các hàm tạm thời mà không cần phải định nghĩa hàm 
        theo cách thông thường.
    - Cú pháp: lambda arguments: expression
        Trong đó:
            arguments: là danh sách các tham số của hàm, được phân cách bằng dấu phẩy.
            expression: là biểu thức mà hàm trả về.
        VD:
            numbers = [1, 2, 3, 4, 5]
            squared_numbers = list(map(lambda x: x**2, numbers))
            
            print(squared_numbers)
            => Đầu ra sẽ là [1, 4, 9, 16, 25].

7. List, Set and Dictionary Comprehensions
    - List Comprehension là một cú pháp cho phép ta tạo ra một danh sách (list) mới bằng cách thực hiện 
        một hoặc nhiều phép biến đổi trên một danh sách hiện có, một cách ngắn gọn và đơn giản hơn 
        so với việc sử dụng vòng lặp for.
    - Cú pháp: new_list = [expression for item in iterable if condition]
        Trong đó: 
            expression: là biểu thức được áp dụng lên từng phần tử của danh sách hiện có, để tạo ra một giá trị 
                mới trong danh sách mới.
            item: là tên biến được sử dụng để đại diện cho từng phần tử của danh sách hiện có.
            iterable: là danh sách hiện có mà ta muốn áp dụng List Comprehension lên.
            condition (tùy chọn): là điều kiện để lọc các phần tử trong danh sách hiện có. Các phần tử 
                không thỏa mãn điều kiện sẽ không được thêm vào danh sách mới.
        VD:
            numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
            even_numbers = [num for num in numbers if num % 2 == 0]
            
            print(even_numbers)
            => Đầu ra sẽ là [2, 4, 6, 8, 10].
    
"""



# Python cơ bản 10
"""
1. Decorators
    - Decorator là một cách để thêm hoặc thay đổi chức năng của một hàm mà không thay đổi mã nguồn của hàm đó. 
        Decorator là một hàm chấm (function wrapper), có thể lấy một hàm làm đối số và trả về một hàm 
        khác mà có chức năng bổ sung.
    - Decorator là một cú pháp đặc biệt bao gồm ký tự @ theo sau là tên của decorator function. 
        Decorator function sẽ được áp dụng trên hàm tiếp theo.
        VD:
            def my_decorator(func):
                def wrapper():
                    print("Trước khi chạy hàm")
                    func()
                    print("Sau khi chạy hàm")
                return wrapper
            
            @my_decorator
            def hello():
                print("Xin chào!")
            
            hello()
            
            => Output: 
                Trước khi chạy hàm
                Xin chào!
                Sau khi chạy hàm

2. Error Handling
    - Error Handling được thực hiện bằng cách sử dụng các câu lệnh try và except. Khi một lỗi xảy ra 
        trong quá trình thực thi chương trình, Python sẽ ném ra một ngoại lệ (exception). 
        Việc sử dụng câu lệnh try và except cho phép chương trình của bạn tiếp tục thực thi bằng cách 
        xử lý ngoại lệ đó một cách chính xác.
    - Cú pháp:
        try:
            # Code có thể gây ra lỗi
        except ExceptionType:
            # Xử lý lỗi
        - Trong đó ExceptionType là loại ngoại lệ cụ thể mà bạn muốn xử lý. Nếu một ngoại lệ được ném ra 
            trong khối try, Python sẽ tìm kiếm câu lệnh except tương ứng và thực thi khối lệnh của nó. 
            Nếu không có câu lệnh except nào tương ứng với loại ngoại lệ đó, chương trình sẽ dừng lại và 
            in ra thông báo lỗi.
        VD:
            try:
                x = 5 / 0
            except ZeroDivisionError:
                print("Lỗi chia cho số 0")
    - Bạn cũng có thể sử dụng nhiều câu lệnh except để xử lý nhiều loại ngoại lệ khác nhau hoặc sử dụng 
        một câu lệnh except chung để xử lý tất cả các loại ngoại lệ. Ngoài ra, bạn có thể sử dụng câu lệnh 
        finally để đảm bảo rằng một khối lệnh được thực thi sau khi một khối try hoặc except đã kết thúc.
        VD:
            try:
                x = 5 / 0
            except ZeroDivisionError:
                print("Lỗi chia cho số 0")
            except TypeError:
                print("Kiểu dữ liệu không hợp lệ")
            finally:
                print("Khối lệnh finally sẽ được thực thi sau khi try hoặc except kết thúc")
    - Ngoài ra, bạn cũng có thể raise (ném ra) một ngoại lệ tùy chỉnh bằng cách sử dụng câu lệnh raise. 
    - Cú pháp của câu lệnh raise như sau: raise ExceptionType("Thông báo lỗi")
    - Trong đó ExceptionType là loại ngoại lệ tùy chỉnh mà bạn muốn raise, và 
        "Thông báo lỗi" là thông báo lỗi tùy chọn để hiển thị cho người dùng.
        VD:
            def divide_numbers(a, b):
                if b == 0:
                    raise ValueError("Cannot divide by zero")
                return a / b
            
            try:
                result = divide_numbers(5, 0)
            except ValueError as e:
                print(e)
        
3. Generators
    - Generators trong Python là một loại hàm đặc biệt, cho phép lặp lại một tập hợp các giá trị 
        một cách dễ dàng. Tuy nhiên, thay vì trả về một danh sách các giá trị như hàm thông thường, 
        generators trả về một iterator, giúp ta lấy ra từng giá trị một khi cần thiết. 
        Điều này giúp giảm thiểu bộ nhớ sử dụng khi lặp qua các tập hợp dữ liệu lớn.
    - Để tạo một generator, chúng ta sử dụng từ khóa yield thay vì return trong hàm. Khi gặp từ khóa yield, 
        hàm sẽ tạm dừng và trả về giá trị hiện tại của generator cho người dùng. Khi hàm được gọi tiếp tục, 
        nó sẽ tiếp tục chạy từ vị trí đã dừng trước đó.
        VD:
            def fibonacci():
                a, b = 0, 1
                while True:
                    yield a
                    a, b = b, a + b
            
            f = fibonacci()
            for i in range(10):
                print(next(f))
        - Trong ví dụ này, chúng ta tạo một generator fibonacci() để sinh ra các số trong dãy Fibonacci. 
            Trong khối while, chúng ta sử dụng từ khóa yield để trả về giá trị hiện tại của generator. 
            Khi chương trình gọi tiếp tục hàm fibonacci(), nó sẽ tiếp tục chạy từ vị trí đã dừng trước đó, 
            giúp chúng ta lặp lại các giá trị trong dãy Fibonacci một cách dễ dàng.
    - Ngoài ra, chúng ta cũng có thể sử dụng các hàm khác để tạo ra generator. 
        VD:
            even_numbers = (x for x in range(10) if x % 2 == 0)
            for i in even_numbers:
                print(i)
        - Trong ví dụ này, chúng ta sử dụng biểu thức generator để tạo ra một danh sách các số chẵn 
            từ 0 đến 10. Với biểu thức generator, chúng ta có thể tạo ra generator mà không cần phải 
            khai báo một hàm mới.

"""



# Python cơ bản 11
"""
1. Bài tập 1:
    - https://www.w3schools.com/quiztest/quiztest.asp?qtest=PYTHON
    
2. Bài tập 2:
    - https://www.w3schools.com/python/exercise.asp
    
3. Bài tập 3:
    - https://github.com/darkprinx/break-the-ice-with-python
    
"""



# Python cơ bản 12
"""
1. Modules 
    - Module là một tập hợp các định nghĩa và các lệnh Python được đóng gói thành một tệp tin có 
        phần mở rộng là .py. Module có thể chứa các hàm, biến, lớp và các đối tượng khác, và được sử dụng 
        để tái sử dụng mã trong nhiều chương trình khác nhau.
    - Các module trong Python cho phép chúng ta tổ chức mã của mình thành các phần có thể sử dụng lại, 
        giúp cho mã của chúng ta trở nên dễ bảo trì hơn. Một số module được cung cấp bởi Python bao gồm:
        - math: chứa các hàm toán học căn bản như sin, cos, tan, sqrt, vv.
        - random: chứa các hàm để sinh số ngẫu nhiên.
        - os: cho phép thao tác với hệ thống tệp.
        - sys: chứa các hàm và biến liên quan đến hệ thống.
        - datetime: chứa các hàm và lớp để làm việc với các đối tượng ngày giờ.
    - Chúng ta có thể sử dụng một module trong một chương trình Python bằng cách sử dụng từ khóa import
    - Ngoài việc import toàn bộ module, chúng ta cũng có thể import một phần của module hoặc đổi tên module.
         VD:
            from math import sqrt
            print(sqrt(16))

2. Packages
    - Package là một tập hợp các module liên quan đến nhau được tổ chức thành một thư mục. 
        Package cũng là một cách để tổ chức mã của chúng ta thành các phần có thể sử dụng lại và 
        giúp cho mã của chúng ta trở nên dễ bảo trì hơn.
    - Một package được biểu diễn bởi một thư mục có chứa một tập hợp các module liên quan đến nhau. 
        Tên của package được xác định bằng tên của thư mục đó, và module được đặt trong các tệp có 
        phần mở rộng là .py trong thư mục đó.
    - Ví dụ, để tạo một package có tên là mypackage, chúng ta có thể tạo một thư mục có tên là mypackage 
        và tạo các module bên trong nó. 
        Cấu trúc thư mục sẽ như sau:
            mypackage/
                __init__.py
                module1.py
                module2.py
    - Trong đó, tệp tin __init__.py là tệp tin đặc biệt được sử dụng để đánh dấu thư mục đó là một package 
        và có thể chứa các lệnh để khởi tạo package.
    - Để sử dụng các module trong package, chúng ta có thể sử dụng các từ khóa import tương tự như khi sử dụng module.
        VD:
            import mypackage.module1

            mypackage.module1.function1()
    - Ngoài việc import toàn bộ module, chúng ta cũng có thể import một phần của module hoặc đổi tên module, 
        tương tự như khi sử dụng module. 
        VD:
            from mypackage.module1 import function1

            function1()       
    
3. __name__
    - Biến __name__ là một biến đặc biệt được sử dụng để xác định tên của module đang được thực thi. 
        Nó được sử dụng để phân biệt giữa việc import module và việc thực thi module đó trực tiếp.
    - Khi một module được import vào một module khác, giá trị của biến __name__ trong module được 
        import sẽ là tên của module đó. Ví dụ, nếu module module1.py được import vào module module2.py, 
        giá trị của biến __name__ trong module1.py sẽ là "module1", trong khi giá trị của biến __name__ 
        trong module2.py sẽ là "module2".
    - Khi một module được thực thi trực tiếp, giá trị của biến __name__ sẽ là "__main__". 
        Điều này cho phép chúng ta xác định xem module đó được thực thi trực tiếp hay chỉ được 
        import vào một module khác.
        VD:
            def main():
                print("Hello, world!")
            
            if __name__ == "__main__":
                main()
        - Trong module này, chúng ta có một hàm main được định nghĩa để thực hiện một số công việc, 
            và có một câu lệnh điều kiện kiểm tra giá trị của biến __name__. Nếu giá trị của biến __name__ 
            là "__main__", tức là module example.py được thực thi trực tiếp, chúng ta sẽ gọi hàm main().
        - Như vậy, nếu chúng ta thực thi module example.py bằng cách chạy lệnh python example.py trong 
            dòng lệnh, hàm main() sẽ được gọi và in ra thông báo "Hello, world!". Tuy nhiên, nếu chúng ta 
            import module example.py vào một module khác, hàm main() sẽ không được gọi. 
            Thay vào đó, module example.py chỉ định nghĩa hàm main() và các thành phần khác của module, 
            và chúng ta có thể sử dụng chúng trong module khác.

4. Built-in Modules
    - Trong Python, có rất nhiều các built-in modules, tức là các module đã được cài đặt sẵn và có thể 
        được sử dụng ngay mà không cần phải cài đặt bổ sung. Các built-in modules này cung cấp các 
        chức năng hữu ích cho các nhu cầu lập trình khác nhau. Dưới đây là một số built-in modules phổ biến 
        trong Python:
            - os: cung cấp các hàm để thao tác với hệ điều hành, như tạo, xóa hoặc di chuyển các file, thư mục.
            - sys: cung cấp các hàm và biến để tương tác với trình thông dịch Python, bao gồm truyền tham số 
                dòng lệnh, thay đổi môi trường hoạt động, xử lý các ngoại lệ...
            - math: cung cấp các hàm toán học, như tính căn bậc hai, lũy thừa, logarit, hàm số siêu khối, v.v.
            - random: cung cấp các hàm để tạo số ngẫu nhiên.
            - datetime: cung cấp các hàm để xử lý thời gian và ngày tháng.
            - re: cung cấp các hàm và ký tự đặc biệt để xử lý các biểu thức chính quy.
            - json: cung cấp các hàm để xử lý các đối tượng JSON.
            - csv: cung cấp các hàm để xử lý các file dữ liệu CSV.
            - urllib: cung cấp các hàm để tương tác với các tài nguyên mạng, như tải về nội dung từ một URL.
            - collections: cung cấp các lớp và hàm để xử lý các cấu trúc dữ liệu phức tạp, như OrderedDict, 
                Counter, defaultdict, v.v.
    - Các built-in modules này có thể được import và sử dụng trong các chương trình Python mà không cần 
        cài đặt thêm bất kỳ thư viện bên ngoài nào. Ngoài các built-in modules, Python còn có rất nhiều 
        thư viện mở rộng được cài đặt từ bên thứ ba, và chúng có thể được cài đặt và sử dụng trong Python 
        để mở rộng chức năng của ngôn ngữ này.
    - Tham khảo các modules tại: https://docs.python.org/3/py-modindex.html
    
5. Python Package Index
    - Python Package Index (Pypi) là kho lưu trữ trực tuyến lớn nhất của các package Python. 
        Nó được sử dụng để cài đặt các package, module và thư viện của Python một cách dễ dàng và nhanh chóng. 
        Pypi cung cấp khoảng 300.000 packages khác nhau, phù hợp với các nhu cầu lập trình khác nhau, 
        từ các công cụ toán học và khoa học đến các công cụ phát triển web và đồ họa.
    - Các packages được đăng tải trên Pypi có thể được cài đặt bằng pip, một công cụ quản lý package 
        được tích hợp sẵn trong Python. Để cài đặt một package từ Pypi, người dùng chỉ cần sử dụng lệnh 
        pip install <package_name> trên dòng lệnh của Python.
    - Pypi cũng cho phép các nhà phát triển tạo và đăng tải các package của riêng họ trên kho lưu trữ 
        trực tuyến này. Việc đăng tải các package trên Pypi giúp cho các package của nhà phát triển trở nên 
        dễ dàng sử dụng hơn cho người dùng Python trên toàn thế giới, đồng thời giúp cho nhà phát triển 
        có thể tiếp cận và phát triển các project mới hơn.
    - Tham khảo tại: https://pypi.org/
    
6. Pip install
    - Trong Python, pip install là một công cụ được tích hợp sẵn để cài đặt và quản lý các package của Python. 
        Pip là viết tắt của "Package Installer for Python" và là công cụ được sử dụng phổ biến nhất để cài đặt 
        các package của Python từ các kho như PyPI (Python Package Index).
    - Khi sử dụng lệnh pip install, người dùng có thể cài đặt một package cụ thể hoặc cập nhật các package 
        đã cài đặt trên hệ thống của mình. Lệnh này có thể được sử dụng từ command line hoặc từ một 
        script Python.
        Câu lệnh: pip install <package>
    - Nếu package đã được cài đặt trên hệ thống của bạn và bạn muốn cập nhật nó, bạn có thể sử dụng lệnh sau:
        pip install --upgrade <package>
    - Ngoài ra, pip cũng cho phép bạn xem các package đã cài đặt trên hệ thống của bạn bằng lệnh pip list, 
        hoặc xem thông tin chi tiết về một package cụ thể bằng lệnh pip show <package_name>.    

7. Debug
    - pdb là một module dùng để debug code. pdb cho phép bạn thực hiện các lệnh debug trên code như in giá trị biến, 
        theo dõi stack trace, đặt breakpoint, step qua từng câu lệnh, vv.
    - Để sử dụng pdb, bạn cần import module pdb và đặt câu lệnh pdb.set_trace() tại nơi bạn muốn bắt đầu debug. 
        Khi chạy chương trình, chương trình sẽ dừng lại tại câu lệnh này và bạn có thể sử dụng các lệnh 
        của pdb để debug code.
    - Ví dụ, để debug một chương trình Python bằng pdb, bạn có thể thực hiện các bước sau:
        Bước 1: Import module pdb vào file Python của bạn:
            import pdb
        Bước 2: Đặt câu lệnh pdb.set_trace() tại điểm bạn muốn bắt đầu debug:
            def my_function():
                pdb.set_trace()
                # Các câu lệnh khác trong hàm
        Bước 3: Chạy chương trình Python. Khi chương trình đến tới câu lệnh pdb.set_trace(), 
            nó sẽ dừng lại và mở terminal cho bạn để thực hiện các lệnh của pdb.
    - Các lệnh của pdb bao gồm:
        - n (next): thực thi câu lệnh tiếp theo
        - s (step): thực thi câu lệnh tiếp theo và bước vào hàm được gọi bởi câu lệnh đó
        - c (continue): tiếp tục thực thi chương trình cho đến khi gặp breakpoint tiếp theo
        - b (break): đặt breakpoint tại một dòng code cụ thể
        - l (list): hiển thị 10 dòng code xung quanh vị trí hiện tại của bạn
        - p (print): in giá trị của một biến
        - q (quit): thoát khỏi pdb và kết thúc chương trình
    
"""



# Python cơ bản 13
"""
1. File I/O
    -  File I/O (Input/Output) được sử dụng để đọc và ghi dữ liệu từ và đến các tệp tin. 
        Các bước cơ bản để thực hiện File I/O trong Python là mở tệp tin, đọc hoặc ghi dữ liệu và đóng tệp tin.
    - Để mở một tệp tin trong Python, ta sử dụng hàm open() với các tham số là đường dẫn tới tệp tin 
        và chế độ mở tệp tin.
        VD: file = open('file.txt', 'r')
    - Trong đó 'file.txt' là đường dẫn tới tệp tin và 'r' là chế độ mở tệp tin cho phép đọc. 
        Các chế độ mở tệp tin thường được sử dụng trong Python bao gồm:
        - 'r': Mở tệp tin để đọc.
        - 'w': Mở tệp tin để ghi (nếu tệp tin không tồn tại sẽ tạo tệp tin mới).
        - 'a': Mở tệp tin để ghi (nếu tệp tin tồn tại thì sẽ ghi tiếp vào cuối tệp tin).
        - 'x': Mở tệp tin để tạo và ghi (nếu tệp tin đã tồn tại thì sẽ báo lỗi).
    - Sau khi mở tệp tin, ta có thể đọc hoặc ghi dữ liệu bằng cách sử dụng các phương thức như 
        read() và write() của đối tượng file.
        VD:
            file = open('file.txt', 'r')
            content = file.read()
            file.close()
        - Trong đó read() được sử dụng để đọc toàn bộ nội dung của tệp tin.
    - Khi kết thúc việc đọc hoặc ghi dữ liệu vào tệp tin, ta cần đóng tệp tin bằng phương thức close(). 
        VD: file.close()
    - Ngoài ra, để đảm bảo rằng tệp tin được đóng một cách đúng đắn, ta có thể sử dụng câu lệnh with để mở tệp tin.
        VD:
            with open('file.txt', 'r') as file:
                content = file.read()
        - Trong đó, khi kết thúc khối lệnh with, tệp tin sẽ tự động được đóng.

2. Read, Write, Append
    - Trong Python, để đọc nội dung của một tệp tin, chúng ta sử dụng phương thức read(). 
        Phương thức này sẽ đọc toàn bộ nội dung của tệp tin và trả về một chuỗi.
        VD:
            with open('file.txt', 'r') as file:
                content = file.read()
                print(content)
    - Để ghi dữ liệu vào một tệp tin, chúng ta sử dụng phương thức write(). 
        Phương thức này sẽ ghi dữ liệu được truyền vào vào cuối tệp tin.
        VD:
            with open('file.txt', 'w') as file:
                file.write('Hello, world!')
    - Để ghi thêm dữ liệu vào cuối tệp tin, chúng ta sử dụng chế độ 'a' (append).
        VD:
            with open('file.txt', 'a') as file:
                file.write('\nThis is a new line.')
     
3. File IO Errors
    - Trong Python, khi thực hiện File I/O, có thể xảy ra một số lỗi như:
        - FileNotFoundError: Khi tệp tin không được tìm thấy.
        - PermissionError: Khi không có quyền truy cập tệp tin.
        - IOError: Khi xảy ra lỗi đọc hoặc ghi dữ liệu vào tệp tin.
        - ValueError: Khi chế độ mở tệp tin không hợp lệ.
        - TypeError: Khi kiểu dữ liệu không hợp lệ được sử dụng trong File I/O.
    - Để xử lý các lỗi này, chúng ta có thể sử dụng câu lệnh try...except trong Python.
        VD:
            try:
                with open('file.txt', 'r') as file:
                    content = file.read()
                    print(content)
            except FileNotFoundError:
                print('File not found.')
            except PermissionError:
                print('Permission denied.')
            except IOError:
                print('Error reading file.')
            except ValueError:
                print('Invalid file mode.')
            except TypeError:
                print('Invalid data type.')
    - Trong đó, try được sử dụng để bắt đầu khối lệnh và except được sử dụng để xử lý lỗi. Nếu xảy ra lỗi, 
        chương trình sẽ nhảy đến khối lệnh except tương ứng và in ra thông báo lỗi.
    - Chúng ta có thể sử dụng nhiều câu lệnh except để xử lý nhiều loại lỗi khác nhau. Ngoài ra, chúng ta 
        cũng có thể sử dụng câu lệnh else trong trường hợp không có lỗi xảy ra và câu lệnh finally để 
        thực hiện một khối lệnh sau khi kết thúc khối lệnh try...except, bất kể có lỗi xảy ra hay không.
"""
