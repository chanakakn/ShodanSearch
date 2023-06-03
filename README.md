# ShodanSearch

Enhancements made to the script include:

Added the logging module to log errors and exceptions to a file (shodan_search.log).

Wrapped the Shodan API calls in try-except blocks to handle and log any exceptions that may occur.

Updated the print_search_result() and print_host_info() functions to handle exceptions more gracefully and log any errors encountered.

Configured the logging level to only log errors or higher (logging.ERROR).

Added a try-except block around the main logic to handle and log any unexpected exceptions.

The addition of logging and exception handling will help in identifying and troubleshooting any errors that occur during the execution of the script. The log file shodan_search.log will contain the error messages.
