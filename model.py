import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import classification_report

# Bước 1: Đọc dữ liệu
data = pd.read_csv('ticket_sales_data.csv')

# Bước 2: Tiền xử lý dữ liệu
# Giả sử 'fraud' là cột nhãn (1 cho gian lận, 0 cho hợp lệ)
X = data.drop('fraud', axis=1)  # Các đặc trưng
y = data['fraud']  # Nhãn

# Chia dữ liệu
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Bước 4: Chọn mô hình
model = RandomForestClassifier()

# Bước 5: Huấn luyện mô hình
model.fit(X_train, y_train)

# Bước 6: Đánh giá mô hình
y_pred = model.predict(X_test)
print(classification_report(y_test, y_pred))