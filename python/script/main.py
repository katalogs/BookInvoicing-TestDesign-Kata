from pathlib import Path
import sys
path_root = Path(__file__).parents[1]
sys.path.append(str(path_root))
print(sys.path)

from src.book_invoicing.report_generator import ReportGenerator


def main() -> None:
    report_generator = ReportGenerator()

    print("****************************************************")
    print("*****************Application Report*****************")
    print("****************************************************")
    print()
    print(f"The total number of books sold is: {report_generator.get_total_sold_books()}")
    print(f"The total number of issued invoices is: {report_generator.get_number_of_issued_invoices()}")
    print(f"The total amount of all invoices in USD is: {report_generator.get_total_amount():,.2f}")
    print()
    print("****************************************************")
    print("****************************************************")


if __name__ == "__main__":
    main()
