import os
import sys
from PIL import Image
from colorama import init, Fore

init(autoreset=True)

converted_count = 0
skipped_count = 0
deleted_count = 0

def get_folder_size(folder_path):
    """Calcula o tamanho total da pasta em bytes."""
    total_size = 0
    for dirpath, dirnames, filenames in os.walk(folder_path):
        for f in filenames:
            fp = os.path.join(dirpath, f)
            total_size += os.path.getsize(fp)
    return total_size

def convert_to_webp(folder_path):
    global converted_count, skipped_count, deleted_count
    supported_formats = (".jpg", ".jpeg", ".png", ".bmp", ".tiff", ".gif")
    
    for root, _, files in os.walk(folder_path):
        for file_name in files:
            file_path = os.path.join(root, file_name)
            
            if file_path.lower().endswith(".webp"):
                print(f"{Fore.YELLOW}Pulado (já em WebP): {file_path}")
                skipped_count += 1
                continue
            
            if file_path.lower().endswith(supported_formats):
                try:
                    with Image.open(file_path) as img:
                        webp_path = os.path.splitext(file_path)[0] + ".webp"
                        img.save(webp_path, "webp")
                        print(f"{Fore.GREEN}Convertido para WebP: {webp_path}")
                        converted_count += 1
                    
                    if file_path.lower().endswith(".png"):
                        os.remove(file_path)
                        print(f"{Fore.RED}PNG removido: {file_path}")
                        deleted_count += 1
                
                except Exception as e:
                    print(f"{Fore.RED}Erro ao converter {file_path}: {e}")

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print(f"{Fore.RED}Por favor, forneça o caminho da pasta.")
    else:
        pasta_imagens = sys.argv[1]
        
        tamanho_inicial = get_folder_size(pasta_imagens)
        
        convert_to_webp(pasta_imagens)
        
        tamanho_final = get_folder_size(pasta_imagens)
        
        print("\n=== Resumo da Execução ===")
        print(f"{Fore.GREEN}Imagens Convertidas para WebP: {converted_count}")
        print(f"{Fore.YELLOW}Imagens Puladas (já em WebP): {skipped_count}")
        print(f"{Fore.RED}Imagens PNG Apagadas: {deleted_count}")
        
        print(f"\n{Fore.CYAN}Tamanho da pasta antes da conversão: {tamanho_inicial / (1024 * 1024):.2f} MB")
        print(f"{Fore.CYAN}Tamanho da pasta após a conversão: {tamanho_final / (1024 * 1024):.2f} MB")
        print(f"{Fore.CYAN}Diferença no tamanho: {(tamanho_inicial - tamanho_final) / (1024 * 1024):.2f} MB")
