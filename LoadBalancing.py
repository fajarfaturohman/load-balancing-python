import threading

class LoadBalancing(threading.Thread):
    def __init__(self, data, start, end):
        threading.Thread.__init__(self)
        self.data = data
        self.start_index = start
        self.end_index = end
        self.result = 0

    def run(self):
        self.result = 0
        for i in range(self.start_index, self.end_index):
            self.result += self.data[i]

        print(f"Thread {self.ident} result: {self.result}")

    def get_result(self):
        return self.result


# Main Program
if __name__ == "__main__":

    # Membuat data 1 sampai 100
    data = [i + 1 for i in range(100)]

    num_threads = 4
    threads = []

    chunk_size = len(data) // num_threads

    # Membuat dan menjalankan thread
    for i in range(num_threads):
        start = i * chunk_size

        if i == num_threads - 1:
            end = len(data)
        else:
            end = start + chunk_size

        thread = LoadBalancing(data, start, end)
        threads.append(thread)
        thread.start()

    total = 0

    # Menunggu semua thread selesai
    for thread in threads:
        thread.join()
        total += thread.get_result()

    print("Total Sum:", total)