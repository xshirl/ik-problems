class Solution:
    def maximumUnits(self, boxTypes: List[List[int]], truckSize: int) -> int:
        boxTypes.sort(key=lambda x: x[1], reverse=True)
        count = 0
        for box in boxTypes:
            boxCount = min(truckSize, box[0])
            count += boxCount * box[1]
            truckSize -= boxCount
            if truckSize == 0:
                break
        return count