import pandas as pd

# Sample data extracted from the OCR content (simplified for demonstration)
data = {
    "Movie_Name": [
        "Onaaigal Ja", "Saavi", "Vidhi Madł", "Bhaagamat", "Mannar Va", "Nimir", 
        "Saranalayam", "Madura Ve", "Savarakath", "Sollividava", "Manushanaa Nee", 
        "Melnaattu", "Naachiyaar", "Nagesh Thi", "Veera", "Kootta", "6 Athiyayaı", 
        "Kaathadi", "Keni", "Merlin", "Tamizhananean Ka", "Yenda Thal", "Dharavi", 
        "Mercury", "Munthal", "Diya", "Paadam", "Pakka", "Sila Samay", "Alai Pesi", 
        "Iruttu Araiy", "Kaathirupp", "Iravukku Ai", "Aaru Mudhal Aaru", "Irumbu Thi", 
        "Nadigaiyar", "Bhaskar Or", "Kilambitaangayaa Kilar", "Andhra Me", "Enna Thavz", 
        "Kargil", "Tik Tik Tik", "Traffic Ram", "Asuravadh", "Ethukadi Kaadhalicha", 
        "Inba Twink", "Semma Bo!", "Kasu Mela", "Mr. Chandı", "Roja Maaligai", 
        "Tamizh Pac", "Kadaikutty", "Mangai Maanvizhi Am", "Bodha", "Maya Bhavanam", 
        "Ondikatta", "Vinveli Pay", "Junga", "Mohini", "Arali", "Enga Kattu", 
        "Ghajinikant", "Kadal Kuthi", "Kadikara M", "Kattu Paya", "Maniyaar k", 
        "Nadodi Kanavu", "Poya Velaya Patthukki", "Azhagumaç", "Kadhal Enakku Romba", 
        "Moondru Rasikarkal", "Pyaar Prem", "Vishwaroo", "Kolamavu i", "Marainthir", 
        "Odu Raja O", "Echcharikk", "Kalari", "Lakshmi", "Merku Tho", "Imaikkaa N", 
        "60 Vayadu", "Aaruthra", "Annanukku", "Avalukkenna Azhagiya", "Padithavudan Kilithu V", 
        "Rajavin Paarvai Raniyir", "Torchlight", "Thodraa", "Vanjagar U", "Seema Raji", 
        "U Turn", "Eghantham", "Medai", "Raja Rangu", "Saamy Squ", "Chekka Chi", 
        "Aadavar", "Pariyerum", "96", "Nota", "Raatchasar", "Yaagan", "Aan Devatl", 
        "Adanga Pasanga", "Amavasai", "Kalavani Sirukki", "Koothan", "Manusang", 
        "Moonavathu Kann", "Vada Cheni", "Ezhumin", "Sandakozhi", "Genius", "Jarugandi", 
        "Raaga Thaalangal", "Santhoshat", "Vanmurai Paguthi", "Billa Pandi", "Kalavani M", 
        "Sarkar", "Kaatrin Mo", "Thimiru Pu", "Utharavu N", "Karimugan", "Karthikeyanum Kaanar", 
        "Pattinapaki", "Sagavaasam", "Sei", "Semmari Aadu", "Vandi", "2", "Dhoni Kabz", 
        "Evanukku E", "Seemathur", "Vinai Ariyar", "Bayangaramana Aalu", "Johnny", "Prabha", 
        "Thiru", "Thulam", "Thuppakki", "Seethakaat", "Adanga Ma", "Kanaa", "Maari 2", 
        "Silukkuvan"
    ],
    "Year": [2018] * 150,  # Assuming all are from 2018 as per the document
    "Director": [
        "Buvanesh", "JPR", "S. Vijai Balz", "G. Ashok", "Boopathy", "Priyadarshi", "Rasu Jegan", 
        "P. G. Muthi", "G. R. Adith", "Arjun", "Ghazali", "MSS", "Bala", "Isaq", "Rajaraman", 
        "S. K. Mathi", "Six director", "Kalyaan", "M. A. Nishá", "Keera", "Sathish", "Vignesh Ka", 
        "Pavithran", "Karthik Sut", "Stunt Jayar", "A. L. Vijay", "Rajashekar", "S. S. Surya", 
        "Priyadarshi", "Murali Bha", "Santhosh P", "Balayya", "Mu. Maran", "M. G. Redd", 
        "P. S. Mithri", "Nag Ashwiı", "Siddique", "Razak", "Jai", "Murabasali", "Sivaani Sen", 
        "Shakti Sour", "Vicky", "Maruthupa", "Ravi Rahul", "R. K. Vidhy", "Badri Venk", 
        "K. S. Pazhal", "Thiru", "Goutham", "C. S. Amud", "Pandiraj", "Vino", "Suresh G.", 
        "Om Shri Ka", "Bharani", "R. Jayaprak", "Gokul", "Madhesh", "A. R. Subba", "Sri Balaji", 
        "Santhosh P", "Pugazhend", "Vaigarai Ba", "Youreka", "Thambi Rai", "Veera Selvi", 
        "Viruthai Ve", "Azhagan Se", "C. Sakthive", "Shebi", "Elan", "Kamal Haa", "Nelson Dili", 
        "Rahesh", "Nishanth, J", "Sarjun", "Kiran Chan", "A. L. Vijay", "Lenin Bhar", "Ajay Gnana", 
        "Radha Mor", "Pa. Vijay", "Rajkumar", "A. Kesavan", "Hari Uttirai", "Azhagu Raj", 
        "Abdul Maji", "Madhu Raj", "Manoj Bee", "Ponram", "Pawan Kun", "Arsal Arum", 
        "S. N. Harira", "Dharani Dh", "Hari", "Mani Ratni", "Sriranjan", "Mari Selvar", 
        "Prem Kumi", "Anand Shai", "Ramkumar", "Vinoth Tha", "Thaamira", "R. Selvanat", 
        "Rakesh Sav", "Ravi Rahul", "Venky AL", "Amshan Ku", "A. V. Giri", "Vetrimaara", 
        "V. P. Viji", "N. Lingusw", "Suseenthir", "A. N. Pitcht", "R. Thirupat", "Kranthi Pra", 
        "Naga", "Saravanasa", "Gandhi Ma", "AR Muruga", "Radha Mol", "Ganeshaa", "Asif Kuraisł", 
        "Chella Thar", "M. A. Bala", "Jayadev", "S. Thomas", "Raj Babu", "Sathish Sut", 
        "Rajeesh Ba", "Shankar", "P. lyappan", "A. R. Muke", "Santhosh T", "K. T. Muruç", 
        "Arasar Raja", "P. Vetriselv", "A. Nanthan", "Karthik Sivi", "Rajanagajo", "Dinesh Seh", 
        "Balaji Thari", "Karthik Tha", "Arunraja Kz", "Balaji Mohi", "Chella"
    ],
    "Studio": [
        "Mukesh Films", "Vasavi Films", "Rite Media", "Studio Gre", "FA3V Cinem", "Moonshot", 
        "Go Production", "P. G. Medi", "Lonewolf P", "Sree Raam", "H3 Cinemas", "Udhaya Cre", 
        "B Studios", "Transindia", "RS Infotain", "SP Pixels", "ASCII Medi", "Galaxy Pictures", 
        "Fragrant Nature Film Creations", "JSB Film Studios", "Vetritamil Vuruvakkam", 
        "Yogi and Partners", "ARS International", "Stone Bench Creations", "Harvest Moon Pictures", 
        "Lyca Productions", "Rollon Movies", "Benn Consortium Studios", "Studios", 
        "Vijayalakshmi Creations", "Blue Ghost Pictures", "Lady Dream Cinemas", "Axess Film Factory", 
        "Sri Lakshmi MGR Movies", "Vishal Film Factory", "Vyjayanthi Movies", "Harshini Movies", 
        "Heaven Entertainment", "Showboat Studios", "Inaindha Kaigal Kalaikoodam", "Sivani Studios", 
        "Thenandal Studio Limited", "Green Signal", "Seven Screen Studios", "Arun Creations", 
        "Appu Movies", "Kickass Entertainment", "Ragav Movie Entertainment", "Creative Entertainers", 
        "1 Look Movies", "Y NOT Studios", "2D Entertainment", "Road Train Pictures", "5050 Films Entertainment", 
        "Ham-Sham Studios", "Friends Cine Media", "Lemurian Thirakkalam", "Vijay Sethupathi Productions", 
        "Marvel Worth Productions", "Am Rm Films", "Vaali Film Visions", "Studio Green", "Global Media Invest", 
        "Christ P International", "White Horse Cinemas", "Vu Cinemas", "RRR Productions", "Harisritha Production", 
        "Avatar Movies", "Win Pictures", "Al-Tari Movies", "K Films", "Aascar Films, Raaj Kamal Films International", 
        "Lyca Productions", "Etcetera Entertainment", "Vijay Moolan Talkies", "Timeline Cinemas", 
        "Nakshatra Movie Magic", "Pramod Films", "Vijay Sethupathi Productions", "Cameo Films India", 
        "V Creations", "Banner Vil Makers", "Grassroot Film Company", "Kathiravan Studios", "Uttirai I Creations", 
        "Vikash Film International", "Confident Film Cafe", "J. S. Aburvaa Production", "Labyrinth Films", 
        "24AM Studios", "Pawan Kumar Studios", "Annai Tamil Cinemas", "Priyam Movie Creations", "Vasan Productions", 
        "Thameens Films", "Lyca Productions, Madras Talkies", "Thambi Deiva Media", "Neelam Productions", 
        "Madras Enterprises", "Studio Green", "Axess Film Factory", "Mappanar Production", "Sigaram Cinemas", 
        "New Vision Creations", "Rakesh Sawant Production", "Rana Creations", "Nilgiris Dream Entertainment", 
        "AK Films", "Arunalaya Cinema", "Wunderbar Films", "Vaiyam Mediyas", "Vishal Film Factory", 
        "Sakthi Film Factory", "Shvedh Group", "Sri Dandayudhapani Movies", "Sree Guru Cinemas", 
        "Aaruthra Cine Productions", "J. K. Film Productions", "Rajapushpa Pictures", "Sun Pictures", 
        "BOFTA Entertainment", "Vijay Antony Film Corporation", "Jaeshan Studios", "A Vimal Production", 
        "Twinkle Labs Production", "SP Cinemas", "Sathiyan Movies", "Trippy Turtle Productions", "Paisa Creations", 
        "Rooby Films", "Lyca Productions", "Manitham Thiraikkalam", "Sai Productions", "Buvan Media Works", 
        "Naagai Films", "Pharristha Pictures", "Staar Movies", "Tamizh Thirai Niruvanam", "Rock Entertainments", 
        "Magical Creations Movies", "V Creations", "Passion Studios", "Home Movie Makers", "Sivakarthikeyan Productions", 
        "Wunderbar Films", "Vishnu Vishal Studioz"
    ],
    "Running_Time": [
        None, None, None, "138 minute", None, None, None, None, None, None, None, "134 minute", 
        "100 minute", None, None, None, "118 minute", None, None, None, None, None, None, None, 
        None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, 
        None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, 
        None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, 
        None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, 
        None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, 
        None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, 
        None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, 
        None, None, None, None, None, None, None, None, None, None, None, None, None, None, None
    ],
    "Release_Date": [
        "13-Dec", None, None, None, None, None, None, None, None, None, None, None, None, None, 
        None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, 
        None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, 
        None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, 
        None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, 
        None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, 
        None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, 
        None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, 
        None, None, None, None, None, None, None, None, None, None, None, None, None, None, None
    ]
}

# Create DataFrame
df = pd.DataFrame(data)

# Function to display the menu and handle user inputs
def movie_dataset_menu():
    while True:
        print("\n=== Movie Dataset Menu ===")
        print("1. Display all movies")
        print("2. Search by Movie Name")
        print("3. Search by Director")
        print("4. Search by Studio")
        print("5. Filter by Year")
        print("6. Exit")
        
        choice = input("Enter your choice (1-6): ")
        
        if choice == "1":
            print(df)
        
        elif choice == "2":
            movie_name = input("Enter movie name to search: ")
            result = df[df["Movie_Name"].str.contains(movie_name, case=False, na=False)]
            if not result.empty:
                print(result)
            else:
                print("No movies found with that name.")
        
        elif choice == "3":
            director = input("Enter director name to search: ")
            result = df[df["Director"].str.contains(director, case=False, na=False)]
            if not result.empty:
                print(result)
            else:
                print("No movies found with that director.")
        
        elif choice == "4":
            studio = input("Enter studio name to search: ")
            result = df[df["Studio"].str.contains(studio, case=False, na=False)]
            if not result.empty:
                print(result)
            else:
                print("No movies found with that studio.")
        
        elif choice == "5":
            year = input("Enter year to filter (e.g., 2018): ")
            try:
                year = int(year)
                result = df[df["Year"] == year]
                if not result.empty:
                    print(result)
                else:
                    print("No movies found for that year.")
            except ValueError:
                print("Please enter a valid year.")
        
        elif choice == "6":
            print("Exiting...")
            break
        
        else:
            print("Invalid choice. Please try again.")

# Run the menu
if __name__ == "__main__":
    movie_dataset_menu()