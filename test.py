import zlib
import re

def is_chinese(s):
    return any('\u4e00' <= c <= '\u9fff' for c in s)

def extract_entries(file_path):
    entries = []
    with open(file_path, 'rb') as f:
        content_bytes = f.read()
        
        while content_bytes:
            try:
                decompressobj = zlib.decompressobj()
                content_decompressed = decompressobj.decompress(content_bytes).decode('utf-8', errors='ignore')
                entries.extend(parse_entries(content_decompressed))
                content_bytes = decompressobj.unused_data
                
            except zlib.error:  # Not a zipfile, skip a byte.
                content_bytes = content_bytes[1:]
                
    return entries


def parse_entries(content):
    # This would depend on the actual structure of the decompressed data.
    # Modify this to suit the actual format of your content.
    # This example assumes each line in the content is a separate word or phrase.
    entries = []
    lines = content.splitlines()
    for line in lines:
        # If the line contains Chinese characters, append it to entries.
        if is_chinese(line):
            entries.append(line)
    return entries

# Replace with your actual file path
file_path = '/System/Library/AssetsV2/com_apple_MobileAsset_DictionaryServices_dictionaryOSX/9cf76a203397f26625fa0c1e9f594f0da5ad7f68.asset/AssetData/Simplified Chinese - English.dictionary/Contents/Resources/Body.data'
chinese_words = extract_entries(file_path)

print(chinese_words)