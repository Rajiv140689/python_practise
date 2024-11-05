# remove duplicate value from the list keeping the first occurance
# Write a Python program to remove duplicates, keep the first occurrence

class DuplicateRemoval():
    def duplicate_removal(self):
        dup_val = [1,1,2,1,2,2,3,4,4,5]
        seen = set()
        non_dup = []

        for dup_val_value in dup_val:
            if dup_val_value not in seen:
                non_dup.append(dup_val_value)
                seen.add(dup_val_value)

        print("non dup value: ", non_dup)

if __name__ == "__main__":
    duplicateRemovalObj1 = DuplicateRemoval()
    duplicateRemovalObj1.duplicate_removal()