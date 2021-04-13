from rest_framework import serializers
from .models import GameBoard, Histories, init_board


# Histories serializer
class HistoriesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Histories
        fields = '__all__'


# GameBoard serializer
class GameBoardSerializer(serializers.ModelSerializer):
    histories = HistoriesSerializer(many=True, read_only=True)

    class Meta:
        model = GameBoard
        fields = ['id', 'owner', 'winner', 'queue', 'players', 'board', 'histories']
        # exclude = ['created']

    def create(self, validated_data):
        board = GameBoard(
            owner=validated_data['owner'],
            queue=validated_data['queue'],
            board_length=validated_data['board_length'],
        )
        board.set_board(init_board(board.board_length))
        board.save()
        return board

    # def update(self, instance, validated_data):
    #     """
    #     Update and return an existing `Snippet` instance, given the validated data.
    #     """
    #     instance.title = validated_data.get('title', instance.title)
    #     instance.code = validated_data.get('code', instance.code)
    #     instance.linenos = validated_data.get('linenos', instance.linenos)
    #     instance.language = validated_data.get('language', instance.language)
    #     instance.style = validated_data.get('style', instance.style)
    #     instance.save()
    #     return instance

