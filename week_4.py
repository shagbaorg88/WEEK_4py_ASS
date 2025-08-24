def file_processor():
    print("📝 File Processor - Text Modifier 📝")
    print("=" * 40)
    
    # Get filename from user with error handling
    while True:
        filename = input("Please enter the filename to read: ").strip()
        
        try:
            # Try to open and read the file
            with open(filename, 'r', encoding='utf-8') as file:
                content = file.read()
            print(f"✅ Successfully read '{filename}'")
            break
            
        except FileNotFoundError:
            print(f"❌ Error: The file '{filename}' does not exist.")
            retry = input("Would you like to try another filename? (y/n): ").lower()
            if retry != 'y':
                print("Exiting program.")
                return
                
        except PermissionError:
            print(f"❌ Error: Permission denied to read '{filename}'.")
            retry = input("Would you like to try another filename? (y/n): ").lower()
            if retry != 'y':
                print("Exiting program.")
                return
                
        except UnicodeDecodeError:
            print(f"❌ Error: Cannot decode the file '{filename}'. It might be a binary file.")
            retry = input("Would you like to try another filename? (y/n): ").lower()
            if retry != 'y':
                print("Exiting program.")
                return
                
        except Exception as e:
            print(f"❌ An unexpected error occurred: {e}")
            retry = input("Would you like to try another filename? (y/n): ").lower()
            if retry != 'y':
                print("Exiting program.")
                return
    
    # Process the content
    print("\nChoose how to modify the file:")
    print("1. Convert to uppercase")
    print("2. Convert to lowercase")
    print("3. Capitalize each sentence")
    print("4. Add line numbers")
    
    while True:
        try:
            choice = int(input("Enter your choice (1-4): "))
            if 1 <= choice <= 4:
                break
            else:
                print("Please enter a number between 1 and 4.")
        except ValueError:
            print("Invalid input. Please enter a number.")
    
    # Apply the chosen modification
    if choice == 1:
        modified_content = content.upper()
        modification_type = "uppercase"
    elif choice == 2:
        modified_content = content.lower()
        modification_type = "lowercase"
    elif choice == 3:
        # Simple sentence capitalization
        sentences = content.split('. ')
        capitalized_sentences = [sentence.capitalize() for sentence in sentences]
        modified_content = '. '.join(capitalized_sentences)
        modification_type = "sentence capitalization"
    else:  # choice == 4
        lines = content.split('\n')
        numbered_lines = [f"{i+1}: {line}" for i, line in enumerate(lines)]
        modified_content = '\n'.join(numbered_lines)
        modification_type = "line numbers"
    
    # Create output filename
    name_parts = filename.rsplit('.', 1)
    if len(name_parts) > 1:
        output_filename = f"{name_parts[0]}_modified.{name_parts[1]}"
    else:
        output_filename = f"{filename}_modified"
    
    # Write the modified content to a new file
    try:
        with open(output_filename, 'w', encoding='utf-8') as file:
            file.write(modified_content)
        print(f"✅ Successfully created '{output_filename}' with {modification_type}")
        
        # Show a preview
        print("\nPreview of modified content:")
        print("-" * 30)
        preview = modified_content[:200] + "..." if len(modified_content) > 200 else modified_content
        print(preview)
        
    except Exception as e:
        print(f"❌ Error writing to file: {e}")

# Run the program
if __name__ == "__main__":
    file_processor()