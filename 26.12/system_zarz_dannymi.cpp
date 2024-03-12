#include<iostream>
#include<fstream>

using namespace std;

#define LB 100

class Pracownik {
public:
    char imie[LB];
    char nazwisko[LB];
    int ID;
    int lista[LB];
    int liczba_projektow;

};

class Project {
public:
    char nazwa[LB];
    int ID_proj;
    char opis[LB];
    char termin[LB];
};

int main() {
    int o = 0;
    int i = 0;
    int wybor;
    int n;
    int m;
    Project b[LB];
    Pracownik a[LB];

    ofstream employerFile("employer.txt");
    ofstream projectFile("project.txt");  

    while (true) {
        cout << "1. Dodaj pracownika. 2. Dodaj projekt. 3. Dodaj pracownika do projektu. 4. Zapisz i wyjdz\n";
        cin >> wybor;

        if (wybor == 1) {
            cout << "Podaj imie pracownika:\n";
            cin >> a[i].imie;
            cout << "Podaj nazwisko pracownika:\n";
            cin >> a[i].nazwisko;
            cout << "Podaj ID pracownika:\n";
            cin >> a[i].ID;
            i++;

            employerFile << "Imie: " << a[i - 1].imie << ", Nazwisko: " << a[i - 1].nazwisko << ", ID: " << a[i - 1].ID << endl;
            continue;
        }

        if (wybor == 2) {
            cout << "Podaj nazwe projektu:\n";
            cin >> b[o].nazwa;
            cout << "Podaj ID projektu:\n";
            cin >> b[o].ID_proj;
            cout << "Podaj opis projektu:\n";
            cin >> b[o].opis;
            cout << "Podaj termin projektu:\n";
            cin >> b[o].termin;
            o++;

            projectFile << "Nazwa projektu: " << b[o - 1].nazwa << ", ID projektu: " << b[o - 1].ID_proj << ", Opis: " << b[o - 1].opis << ", Termin: " << b[o - 1].termin << endl;
            continue;
        }

        if (wybor == 3) {
            cout << "Podaj ID pracownika:\n";
            cin >> n;
            cout << "Podaj ID projektu:\n";
            cin >> m;

                a[n].lista[a[n].liczba_projektow] = m;
                a[n].liczba_projektow++;
            
            continue;
        }

        if (wybor == 4) {
            for (int j = 0; j < i; ++j) {
                employerFile << "Imie: " << a[j].imie << ", Nazwisko: " << a[j].nazwisko << ", ID: " << a[j].ID << endl;
            }

            for (int k = 0; k < o; ++k) {
                projectFile << "Nazwa projektu: " << b[k].nazwa << ", ID projektu: " << b[k].ID_proj << ", Opis: "
                            << b[k].opis << ", Termin: " << b[k].termin << endl;
            }

        
            employerFile.close();
            projectFile.close();
            break;
        }
    }

    return 0;
}
