const i16 DEFAULT_LIST_SIZE = 10

typedef i32 timestamp

enum PhoneType {
    MOBILE,
    HOME,
    WORK,
}

struct PhoneNumber {
    1: optional PhoneType type = 0,
    2: optional string number,
}

struct Person {
    1: optional string name,
    2: optional list<PhoneNumber> phones,
    4: optional timestamp created_at,
}

typedef map<string, Person> PersonMap

struct AddressBook {
    1: optional PersonMap people,
}

exception PersonNotExistsError {
    1: optional string message = "Person Not Exists!",
}

service AddressBookService {
    void ping();
    string hello(1: string name);
    bool add(1: Person person);
    bool remove(1: string name) throws (1: PersonNotExistsError not_exists);
    Person get(1: string name) throws (1: PersonNotExistsError not_exists);
    AddressBook book();
    list<PhoneNumber> get_phonenumbers(1: string name, 2: i32 count);
    map<PhoneType, string> get_phones(1: string name);
    bool sleep(1: i16 ms);
}
