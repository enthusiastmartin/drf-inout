## drf-inout

Support for different serializers in a view for Django Rest Framework

### Installation

```
pip install drf-inout
```

### Usage
```
from drf_inout.mixins import InOutSerializerMixin


class YourSerializer(InOutSerializerMixin, ModelSerializer):
   in_serializer_class = YourInSerializer # used for POST/PUT/PATCH requests
   out_serializer_class = YourOutSerializer # used for GET requests
```
