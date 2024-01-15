<?php

namespace App\Models;

use Dcat\Admin\Traits\HasDateTimeFormatter;
use Illuminate\Database\Eloquent\Relations\BelongsToMany;
use Illuminate\Database\Eloquent\SoftDeletes;
use Illuminate\Database\Eloquent\Model;

class Scheduling extends Model
{
	use HasDateTimeFormatter;
    use SoftDeletes;

    public function place(): BelongsToMany
    {
        return $this->belongsToMany(Place::class);
    }
    }
