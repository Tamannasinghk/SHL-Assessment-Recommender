import pandas as pd
import random
from faker import Faker

fake = Faker()
Faker.seed(0)
random.seed(0)

# Sample categories for test types .
test_types = ['A', 'B', 'C', 'D', 'E', 'F', 'K', 'P', 'M', 'N']

# Generating fake dataset .
data = []
for i in range(1000):
    name = fake.catch_phrase()
    remote_testing = random.choice(['yes', 'no'])
    adaptive_irt = random.choice(['yes', 'no'])
    test_type = ' '.join(random.sample(test_types, random.randint(1, 4)))
    duration = f"{random.randint(10, 90)} min" if random.random() > 0.1 else "NAN"
    description = fake.paragraph(nb_sentences=3)
    url_suffix = '-'.join(name.lower().split())
    url = f"https://www.shl.com/products/product-catalog/view/{url_suffix}/"

    data.append({
        'assesment_name': name,
        'remote_testing': remote_testing,
        'Adaptive/IRT': adaptive_irt,
        'Test Type': test_type,
        'duration': duration,
        'description': description,
        'URL': url
    })

# Converting to DataFrame and saving to CSV .
df = pd.DataFrame(data)
csv_path = "fake_shl_assessments.csv"
df.to_csv(csv_path, index=False)

csv_path
