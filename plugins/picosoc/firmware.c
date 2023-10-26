
#include <stdint.h>
#include <stdbool.h>

extern uint32_t sram;

#define reg_uart_clkdiv (*(volatile uint32_t*)0x02000004)
#define reg_uart_data (*(volatile uint32_t*)0x02000008)
#define reg_leds (*(volatile uint32_t*)0x03000000)

// --------------------------------------------------------

void putchar(char c)
{
	if (c == '\n')
		putchar('\r');
	reg_uart_data = c;
}

void print(const char *p)
{
	while (*p)
		putchar(*(p++));
}


// --------------------------------------------------------

void main()
{
	reg_uart_clkdiv = 868;
	print("Booting..\n");

	while (1)
	{
		print("Select an action:\n");
	}
}
