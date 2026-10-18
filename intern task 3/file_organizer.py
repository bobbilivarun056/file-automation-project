import os
import shutil
import logging

# Logging setup
logging.basicConfig(
    filename="file_organizer.log",
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)

# File categories
FILE_CATEGORIES = {
    "Images": [".jpg", ".jpeg", ".png", ".gif"],
    "Documents": [".pdf", ".doc", ".docx", ".txt"],
    "Audio": [".mp3", ".wav", ".aac"],
    "Videos": [".mp4", ".avi", ".mkv"],
    "Archives": [".zip", ".rar", ".7z"]
}


def get_category(filename):
    extension = os.path.splitext(filename)[1].lower()

    for category, extensions in FILE_CATEGORIES.items():
        if extension in extensions:
            return category

    return "Others"


def organize_files(folder_path):

    try:
        if not os.path.exists(folder_path):
            print("Folder does not exist.")
            logging.error("Folder does not exist: %s", folder_path)
            return

        if not os.path.isdir(folder_path):
            print("The given path is not a folder.")
            logging.error("Path is not a folder: %s", folder_path)
            return

        files = os.listdir(folder_path)

        for filename in files:

            source_path = os.path.join(folder_path, filename)

            # Skip folders
            if os.path.isdir(source_path):
                continue

            category = get_category(filename)

            category_folder = os.path.join(
                folder_path,
                category
            )

            # Create category folder
            if not os.path.exists(category_folder):
                os.makedirs(category_folder)

            destination_path = os.path.join(
                category_folder,
                filename
            )

            # Move file
            shutil.move(
                source_path,
                destination_path
            )

            print(
                f"Moved: {filename} -> {category}/"
            )

            logging.info(
                "Moved %s -> %s",
                filename,
                category_folder
            )

        print("\nFile organization completed successfully.")

        logging.info(
            "File organization completed."
        )

    except PermissionError:

        print(
            "Permission denied. Check folder permissions."
        )

        logging.exception(
            "Permission denied."
        )

    except Exception as e:

        print(
            f"An unexpected error occurred: {e}"
        )

        logging.exception(
            "Unexpected error occurred."
        )


def main():

    print("===================================")
    print("      FILE ORGANIZER AUTOMATION")
    print("===================================")

    folder_path = input(
        "Enter the folder path to organize: "
    ).strip()

    organize_files(folder_path)


if __name__ == "__main__":
    main()