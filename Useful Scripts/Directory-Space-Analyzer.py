import os
from tqdm import tqdm
from rich.console import Console
from rich.table import Table
from rich.prompt import Confirm

# Initialize a rich Console for colorful output
console = Console()


def get_size(path):
    """Calculate the size of a file or directory."""
    total = 0
    if os.path.isfile(path):
        return os.path.getsize(path)
    elif os.path.isdir(path):
        for dirpath, dirnames, filenames in os.walk(path):
            for filename in filenames:
                filepath = os.path.join(dirpath, filename)
                total += os.path.getsize(filepath)
    return total


def format_size(bytes_size):
    """Format size from bytes to KB, MB"""
    if bytes_size >= 1024 * 1024:
        return f"{bytes_size / (1024 * 1024):.2f} MB"
    elif bytes_size >= 1024:
        return f"{bytes_size / 1024:.2f} KB"
    else:
        return f"{bytes_size} bytes"


def analyze_space(directory):
    """Analyze directory space usage and display in a table format."""
    files = []
    folders = []
    total_size = 0

    entries = list(os.scandir(directory))

    with tqdm(
        total=len(entries), desc="Analyzing directory entries", unit="entry"
    ) as pbar:
        for entry in entries:
            if entry.is_file():
                size = get_size(entry.path)
                files.append((entry.name, size))
                total_size += size
            elif entry.is_dir():
                size = get_size(entry.path)
                folders.append((entry.name, size))
                total_size += size
            pbar.update(1)

    # Sort files and folders by size (descending)
    sorted_files = sorted(files, key=lambda x: x[1], reverse=True)
    sorted_folders = sorted(folders, key=lambda x: x[1], reverse=True)

    # Display results in a rich table format
    console.print("\n[bold cyan]Files:[/bold cyan]")
    file_table = Table(title="Files", show_header=True, header_style="bold magenta")
    file_table.add_column("File Name", style="dim", width=40)
    file_table.add_column("Size", justify="right")

    for file in sorted_files:
        file_table.add_row(file[0], format_size(file[1]))

    console.print(file_table)

    console.print("\n[bold cyan]Folders:[/bold cyan]")
    folder_table = Table(title="Folders", show_header=True, header_style="bold magenta")
    folder_table.add_column("Folder Name", style="dim", width=40)
    folder_table.add_column("Size", justify="right")

    for folder in sorted_folders:
        folder_table.add_row(folder[0], format_size(folder[1]))

    console.print(folder_table)

    # Display total directory size
    console.print(
        f"\n[bold yellow]Total Directory Size:[/bold yellow] {format_size(total_size)}"
    )

    # Option to save log to file
    if Confirm.ask("\nDo you want to save this log to a file?", default=False):
        save_log(directory, sorted_files, sorted_folders, total_size)


def save_log(directory, files, folders, total_size):
    """Save analyzed data to a log file."""
    log_file = os.path.join(directory, "space_analysis_log.txt")
    with open(log_file, "w") as f:
        f.write("Space Analysis Report\n")
        f.write(f"Directory: {directory}\n\n")

        f.write("Files:\n")
        for file in files:
            f.write(f"{file[0]}: {format_size(file[1])}\n")

        f.write("\nFolders:\n")
        for folder in folders:
            f.write(f"{folder[0]}: {format_size(folder[1])}\n")

        f.write(f"\nTotal Directory Size: {format_size(total_size)}\n")

    console.print(f"\n[green]Log saved to {log_file}[/green]")


if __name__ == "__main__":
    directory = input("Enter the directory path: ")
    if os.path.isdir(directory):
        analyze_space(directory)
    else:
        console.print("[red]Error: Invalid directory path[/red]")
