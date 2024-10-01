#include <BLEDevice.h>
#include <BLEUtils.h>
#include <BLEScan.h>

BLEScan* pBLEScan;

class MyAdvertisedDeviceCallbacks : public BLEAdvertisedDeviceCallbacks {
    void onResult(BLEAdvertisedDevice advertisedDevice) {
        Serial.print("Найдено устройство: ");
        Serial.println(advertisedDevice.getAddress().toString().c_str());

        if (advertisedDevice.haveName()) {
            Serial.print("Имя: ");
            Serial.println(advertisedDevice.getName().c_str());
        }

        Serial.print("RSSI: ");
        Serial.println(advertisedDevice.getRSSI());

        Serial.print("Рекламные данные: ");
        String advData = advertisedDevice.getManufacturerData();
        for (int i = 0; i < advData.length(); i++) {
            Serial.printf("%02X ", advData[i]);
        }
        Serial.println();
    }
};

void setup() {
    Serial.begin(115200);
    
    BLEDevice::init("");
    pBLEScan = BLEDevice::getScan();
    pBLEScan->setAdvertisedDeviceCallbacks(new MyAdvertisedDeviceCallbacks());
    pBLEScan->setActiveScan(false);
    pBLEScan->setInterval(100);
    pBLEScan->setWindow(99);
    
    Serial.println("Запуск сканирования BLE...");
}

void loop() {
    pBLEScan->start(10, false);
    pBLEScan->clearResults();
}
