
#include <stdlib.h>
#include <math.h>
#include <stdint.h>
#include <stdbool.h>
#include <registers.h>


// --------------------------------------------------------

void putchar(char c) {
	if (c == '\n') {
		putchar('\r');
    }
	reg_uart_data = c;
}

void print(const char *p) {
	while (*p) {
		putchar(*(p++));
    }
}

char getchar_prompt(char *prompt) {
	int32_t c = -1;

	uint32_t cycles_begin, cycles_now, cycles;
	__asm__ volatile ("rdcycle %0" : "=r"(cycles_begin));

	reg_gpio = ~0;

	if (prompt) {
		print(prompt);
    }

	while (c == -1) {
		__asm__ volatile ("rdcycle %0" : "=r"(cycles_now));
		cycles = cycles_now - cycles_begin;
		if (cycles > PICOSOC_CLOCK / 2) {
			if (prompt) {
				print(prompt);
            }
			cycles_begin = cycles_now;
			reg_gpio = ~reg_gpio;
		}
		c = reg_uart_data;
	}

	reg_gpio = 0;
	return c;
}

char getchar() {
	return getchar_prompt(0);
}

// --------------------------------------------------------

void cmd_echo() {
	print("Return to menu by sending '!'\n\n");
	char c;
	while ((c = getchar()) != '!') {
		putchar(c);
    }
}


// Funktion zum Austauschen zweier Zahlen
void swap(char *x, char *y) {
    char t = *x; *x = *y; *y = t;
}
 
// Funktion zum Umkehren von `buffer[i…j]`
char* reverse(char *buffer, int i, int j)
{
    while (i < j) {
        swap(&buffer[i++], &buffer[j--]);
    }
 
    return buffer;
}
 
// Iterative Funktion zum Implementieren der Funktion `itoa()` in C
char* itoa(int value, char* buffer, int base)
{
    // Ungültige Eingabe
    if (base < 2 || base > 32) {
        return buffer;
    }
 
    // berücksichtige den absoluten Wert der Zahl
    //int n = abs(value);
    int n = value;
    if (value < 0) {
        n = -value;
    }
 
    int i = 0;
    while (n)
    {
        int r = n % base;
 
        if (r >= 10) {
            buffer[i++] = 65 + (r - 10);
        }
        else {
            buffer[i++] = 48 + r;
        }
 
        n = n / base;
    }
 
    // wenn die Zahl 0 ist
    if (i == 0) {
        buffer[i++] = '0';
    }
 
    // Wenn die Basis 10 ist und der Wert negativ ist, der resultierende String
    // vorangestellt ist ein Minuszeichen (-)
    // Bei jeder anderen Basis gilt der Wert immer als unsigned
    if (value < 0 && base == 10) {
        buffer[i++] = '-';
    }
 
    buffer[i] = '\0'; // Null-Terminierungszeichenfolge
 
    // den String umkehren und zurückgeben
    return reverse(buffer, 0, i - 1);
}


void main() {
    char buffer[33];

	reg_uart_clkdiv = UART_CLOCK_DIV;
	print("Booting..\n");


	while (getchar_prompt("Press ENTER to continue..\n") != '\r') {
        /* wait */ 
    }

	print("\n");
	print("  ____  _ \n");
	print(" |  _ \\ _  ___\n");
	print(" | |_) | |/ _ \\ \n");
	print(" |    /| | (_) |\n");
	print(" |_|\\_\\|_|\\___/ \n");
	print("\n");

	print("\n");

	while (1) {
		print("\n");

		print("Select an action:\n");
		print("\n");
		print("   [e] Echo UART\n");
		print("\n");

		for (int rep = 10; rep > 0; rep--) {

            reg_gpio = ~reg_gpio;


            print(itoa(reg_counter, buffer, 10));
            print("\n");

            print(itoa(reg_sysclock, buffer, 10));
            print("\n");

			print("Command> ");
			char cmd = getchar();
			if (cmd > 32 && cmd < 127) {
				putchar(cmd);
            }
			print("\n");

			switch (cmd) {
                case 'e':
                    cmd_echo();
                    break;
                case 'r':
                    reg_counter = 100;
                    break;
                default:
                    continue;
			}
			break;
		}
	}
}
