
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
		if (cycles > 12000000) {
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

void print_dec(uint32_t v)
{
	if (v >= 1000) {
		print(">=1000");
		return;
	}

	if      (v >= 900) { putchar('9'); v -= 900; }
	else if (v >= 800) { putchar('8'); v -= 800; }
	else if (v >= 700) { putchar('7'); v -= 700; }
	else if (v >= 600) { putchar('6'); v -= 600; }
	else if (v >= 500) { putchar('5'); v -= 500; }
	else if (v >= 400) { putchar('4'); v -= 400; }
	else if (v >= 300) { putchar('3'); v -= 300; }
	else if (v >= 200) { putchar('2'); v -= 200; }
	else if (v >= 100) { putchar('1'); v -= 100; }

	if      (v >= 90) { putchar('9'); v -= 90; }
	else if (v >= 80) { putchar('8'); v -= 80; }
	else if (v >= 70) { putchar('7'); v -= 70; }
	else if (v >= 60) { putchar('6'); v -= 60; }
	else if (v >= 50) { putchar('5'); v -= 50; }
	else if (v >= 40) { putchar('4'); v -= 40; }
	else if (v >= 30) { putchar('3'); v -= 30; }
	else if (v >= 20) { putchar('2'); v -= 20; }
	else if (v >= 10) { putchar('1'); v -= 10; }

	if      (v >= 9) { putchar('9'); v -= 9; }
	else if (v >= 8) { putchar('8'); v -= 8; }
	else if (v >= 7) { putchar('7'); v -= 7; }
	else if (v >= 6) { putchar('6'); v -= 6; }
	else if (v >= 5) { putchar('5'); v -= 5; }
	else if (v >= 4) { putchar('4'); v -= 4; }
	else if (v >= 3) { putchar('3'); v -= 3; }
	else if (v >= 2) { putchar('2'); v -= 2; }
	else if (v >= 1) { putchar('1'); v -= 1; }
	else putchar('0');
}

void main() {
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

            print_dec(reg_counter);
            print("\n");

            print_dec(reg_sysclock);
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
