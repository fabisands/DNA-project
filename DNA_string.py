from PIL import Image, ImageDraw, ImageFont

# Function to add a nucleotide image with a letter
def add_nucleotide(image, letter, nucleotide_path):
    nucleotide = Image.open(nucleotide_path)
    image.paste(nucleotide, (image.width, 0))
    draw = ImageDraw.Draw(image)
    font = ImageFont.load_default()
    draw.text((image.width + 20, 20), letter, fill="black", font=font)
    return image

# Function to create an empty canvas for the DNA strand
def create_dna_canvas(width, height):
    return Image.new("RGBA", (width, height), (255, 255, 255, 0))

if __name__ == "__main__":
    # Set the canvas dimensions and initial nucleotide
    canvas_width = 100
    canvas_height = 100
    dna_canvas = create_dna_canvas(canvas_width, canvas_height)

    # Input your DNA sequence as a string of letters (e.g., "ATCGATCG")
    dna_sequence = input("Enter your DNA sequence: ")

    for letter in dna_sequence:
        if letter.upper() == "A":
            nucleotide_path = r"C:\Users\faren\OneDrive - Universidad de la Amazonia\Documents\GitHub\Nucleotide_A5.jpeg"
        elif letter.upper() == "T":
            nucleotide_path = r"C:\Users\faren\OneDrive - Universidad de la Amazonia\Documents\GitHub\Nucleotide_T5.jpeg"
        elif letter.upper() == "C":
            nucleotide_path = r"C:\Users\faren\OneDrive - Universidad de la Amazonia\Documents\GitHub\Nucleotide_C5.jpeg"
        elif letter.upper() == "G":
            nucleotide_path = r"C:\Users\faren\OneDrive - Universidad de la Amazonia\Documents\GitHub\Nucleotide_G5.jpeg"
        else:
            print(f"Ignoring invalid letter: {letter}")
            continue

        dna_canvas = add_nucleotide(dna_canvas, letter, nucleotide_path)

    # Save the final DNA strand image
    dna_canvas.show()
    dna_canvas.save("DNA_strand.png")
