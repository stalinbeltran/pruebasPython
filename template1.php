{{=<< >>=}}
<?php

namespace App\Models;

use Illuminate\Database\Eloquent\Factories\HasFactory;
use Illuminate\Database\Eloquent\Model;

class <<NombreClase>> extends Model
{
    use HasFactory;

    protected $table = '<<NombreTabla>>';
    public $timestamps = true;

    protected $casts = [
    ];

    protected $fillable = [
        <<#fillable>>
        '<<campo>>',
        <</fillable>>
    ];

    <<>funcionesRelacion>>
    
}
