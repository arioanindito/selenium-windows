"This application is for calculates URL web console performance"

import unittest
import json
from selenium import webdriver

class Test(unittest.TestCase):
    "This class is to calculate URL Performance and produce the required report files"

    def setUp(self):
        "This is the webdriver configuration"
        self.driver = webdriver.Chrome(r"D:\Ario Anindito\University Stuff\Cardiff University & VUM\3. Winter 2021\Software Metrics\selenium-master\chromedriver.exe")
        self.driver.implicitly_wait(30)
        self.verification_errors = []

    def test_er(self):
        """
        The main function that runs URL performance for 10 times.
        Furthermore, it will generates csv, txt, and json files, while calculates
        mean average of the performance.
        :return:
        """
        driver = self.driver
        total = {}

        # this creates an output.txt file and appends the name and duration
        with open("result.txt", "w") as json_file:
            for result in range(10):
                driver.get("https://en.wikipedia.org/wiki/Software_metric")
                result = driver.execute_script("return window.performance.getEntries()")

                for current in result:
                    url = current["name"]
                    current_list = total.get(url, [])
                    current_list.append(current["duration"])
                    total[url] = current_list
                    json_file.write(f"{current['name']}, {current['duration']}\n")

        # This creates a csv file and calculates the average duration and appends it to the csv file
        with open("result_in_csv.csv", "w") as csv_file:
            for key, value in total.items():
                average = sum(value) / len(total)
                csv_file.write(f"{key}, {average}\n")

        # This makes a JSON output file and prettifies it
        with open("output_json" + ".json", "w", encoding="utf-8") as file:
            json.dump(result, file, ensure_ascii=False, indent=4)

    def tearDown(self):
        self.driver.quit()
        self.assertEqual([], self.verification_errors)


if __name__ == "__main__":
    unittest.main()

    #s = unittest.TestLoader().loadTestsFromTestCase(Test)
    #unittest.TextTestRunner().run(s)
