<?php

namespace App\Models;

use Dcat\Admin\Traits\HasDateTimeFormatter;
use Illuminate\Database\Eloquent\Relations\BelongsTo;
use Illuminate\Database\Eloquent\SoftDeletes;
use Illuminate\Database\Eloquent\Model;

class Project extends Model
{
    use HasDateTimeFormatter;
    use SoftDeletes;

    protected $fillable = ['name', 'options', 'photo', 'video'];

    public function place(): BelongsTo
    {
        return $this->belongsTo(Place::class, 'place_id');
    }
}
