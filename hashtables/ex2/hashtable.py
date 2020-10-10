class HashTableEntry:
    """
    Linked List hash table key/value pair
    """
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.next = None


# Hash table can't have fewer than this many slots
MIN_CAPACITY = 8


class HashTable:
    """
    A hash table that with `capacity` buckets
    that accepts string keys

    Implement this.
    """

    def __init__(self, capacity):
        self.bucket_array = [None for i in range(capacity)];
        self.capacity = capacity;
        self.count = 0;


    def get_num_slots(self):
        """
        Return the length of the list you're using to hold the hash
        table data. (Not the number of items stored in the hash table,
        but the number of slots in the main list.)

        One of the tests relies on this.

        Implement this.
        """
        return len(self.bucket_array);


    def get_load_factor(self):
        """
        Return the load factor for this hash table.

        Implement this.
        """
        return self.count / self.capacity;


    def fnv1(self, key):
        """
        FNV-1 Hash, 64-bit

        Implement this, and/or DJB2.
        """

        # Your code here


    def djb2(self, key):
        """
        DJB2 hash, 32-bit

        Implement this, and/or FNV-1.
        """
        hash = 5381
        byte_array = key.encode('utf-8');

        for byte in byte_array:
            hash = ((hash * 33) ^ byte) % 0x100000000
        return hash


    def hash_index(self, key):
        """
        Take an arbitrary key and return a valid integer index
        between within the storage capacity of the hash table.
        """
        #return self.fnv1(key) % self.capacity
        return self.djb2(key) % self.capacity

    def put(self, key, value):
        """
        Store the value with the given key.

        Hash collisions should be handled with Linked List Chaining.

        Implement this.
        """
        bucket_index = self.hash_index(key);
        new_entry = HashTableEntry(key, value);

        existing_entry = self.bucket_array[bucket_index];

        if existing_entry:
            last_entry = None
            while existing_entry:
                if existing_entry.key == key:
                    existing_entry.value = value
                    return
                last_entry = existing_entry
                existing_entry = existing_entry.next
            last_entry.next = new_entry
            self.count += 1;
        else:
            self.bucket_array[bucket_index] = new_entry;
            self.count += 1;



    def delete(self, key):
        """
        Remove the value stored with the given key.

        Print a warning if the key is not found.

        Implement this.
        """
        bucket_index = self.hash_index(key);

        existing_entry = self.bucket_array[bucket_index];

        if existing_entry:
            last_entry = None
            while existing_entry:
                if existing_entry.key == key:
                    if last_entry:
                        last_entry.next = existing_entry.next
                    else:
                        self.bucket_array[bucket_index] = existing_entry.next
                        self.count -= 1;
                    last_entry = existing_entry
                    existing_entry = existing_entry.next
                    self.count -= 1;


    def get(self, key):
        """
        Retrieve the value stored with the given key.

        Returns None if the key is not found.

        Implement this.
        """
        bucket_index = self.hash_index(key);
        existing_entry = self.bucket_array[bucket_index]

        if existing_entry:
            if existing_entry.next == None:
                return existing_entry.value
            else:
                while existing_entry:
                    if existing_entry.key == key:
                        return existing_entry.value
                    existing_entry = existing_entry.next
        return None


    def resize(self, new_capacity):
        """
        Changes the capacity of the hash table and
        rehashes all key/value pairs.

        Implement this.
        """
        old_bucket = self.bucket_array
        self.bucket_array = [None for i in range(new_capacity)];

        for entry in old_bucket:
            if entry.next == None:
                self.put(entry.key,entry.value)
            else:
                while entry:
                    self.put(entry.key,entry.value)
                    entry = entry.next
