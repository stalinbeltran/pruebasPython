<?php

namespace App\Models;

use Illuminate\Database\Eloquent\Factories\HasFactory;
use Illuminate\Database\Eloquent\Model;

class Usuario extends Model
{
    use HasFactory;

    protected $table = 'usuario';
    public $timestamps = true;

    protected $casts = [
    ];

    protected $fillable = [
        'usuario',
        'password',
        'email',
        'nombre',
        'activedirectory',
    ];

    public function grupos()
        {
            return $this->belongsToMany(Grupo::class);
        }    
}
