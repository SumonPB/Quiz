from django.http import JsonResponse
from rest_framework.views import APIView
from rest_framework.response import Response
from .serializers import QuestionSerializer  # Asegúrate de tener este serializador

from django.views import View
import json
from .models import Question, Answer
from django.views.decorators.csrf import csrf_exempt

class QuestionListView(APIView):
    def get(self, request, *args, **kwargs):
        questions = Question.objects.all()
        serializer = QuestionSerializer(questions, many=True)
        return Response(serializer.data)


class UploadQuestionsView(View):

    @csrf_exempt
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        # Verifica si se envió un archivo
        if 'file' not in request.FILES:
            return JsonResponse({"error": "No file provided"}, status=400)

        file = request.FILES['file']

        try:
            # Lee y parsea el archivo JSON
            data = json.load(file)
            
            # Verifica que los datos sean una lista
            if not isinstance(data, list):
                return JsonResponse({"error": "Invalid data. Expected a list."}, status=400)

            # Procesa cada pregunta en la lista
            for item in data:
                # Crea la pregunta
                question = Question.objects.create(
                    question_type=item['question_type'],
                    text=item['text']
                )
                # Crea las respuestas asociadas
                for answer in item['answers']:
                    Answer.objects.create(
                        question=question,
                        text=answer['text'],
                        is_correct=answer['is_correct']
                    )
            return JsonResponse({"message": "File uploaded successfully"}, status=200)
        except json.JSONDecodeError as e:
            return JsonResponse({"error": f"JSON parse error: {str(e)}"}, status=400)
        except KeyError as e:
            return JsonResponse({"error": f"Missing key in JSON: {str(e)}"}, status=400)
        except Exception as e:
            return JsonResponse({"error": str(e)}, status=500)